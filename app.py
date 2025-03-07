import os
import tempfile
from dotenv import load_dotenv
from langchain import PromptTemplate
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from collections import defaultdict

import json

import json


def save_answer(answers: dict, file_name: str):
    with open(f"./answer/{file_name}", "w", encoding="utf-8") as fp:
        json.dump(answers, fp, indent=2, ensure_ascii=True)


def read_answers(file_name: str) -> dict:
    if os.path.exists(f"./answer/{file_name}"):
        with open(f"./answer/{file_name}", "r") as fp:
            answers = json.load(fp)
            return answers
    else:
        return dict()


def convert_json_to_md(file_name):
    answers = read_answers(file_name)
    lines = []
    for question, answer_details in answers.items():
        answer = answer_details.get("answer")
        pages = answer_details.get("pages")
        lines.append(f"### {question}\n")
        lines.append(f"{answer}\n")
        lines.append(f" - Source: {pages}\n\n\n")
    with open(f"./answer/{file_name.replace('.json', '.md')}", "w") as f:
        f.writelines(lines)


file_name = "DWT_answers.json"
answers_dict = read_answers(file_name=file_name)


def main():
    load_dotenv()

    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF 💬")

    # upload file
    pdf = st.file_uploader("Upload your PDF", type="pdf")
    # extract the text
    if pdf is not None:
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(pdf.read())
            print("Re-writing the file")
            file_name = f.name

        page_offset = get_offset_by_name(pdf.name)
        loader = PyPDFLoader(file_name)
        data = loader.load()

        # create embeddings
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_documents(data, embeddings)

        # show user input
        user_question = st.text_area("Ask a question about your PDF:")
        prompt_template = """
    Follow the instructions below to answer the question:
    - Use the following pieces of context inside triple quotes to answer the question
    - Question will be outside the triple quotes
    - Answer in brief between 70-150 words

    '''{context}'''

    Question: {question}
    Answer:
    """
        prompt = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
        )
        if user_question:
            docs = knowledge_base.similarity_search(user_question)
            for doc in docs:
                doc.page_content = doc.page_content.encode("utf-8", "replace").decode()
            # print(docs)
            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)
            with get_openai_callback() as cb:
                response = chain.run(
                    input_documents=docs, question=user_question, max_tokens=4000
                )
                print(cb)

            filename = "answers.json"
            answers_dict = read_answers(file_name=filename)
            details = defaultdict()
            details["answer"] = response
            details["pages"] = [
                int(doc.metadata.get("page")) + page_offset for doc in docs
            ]
            print(details)
            response = response.replace("\n", "\n\n")
            response += "\n\n"
            response += f" - Source: {details['pages']}\n\n\n"
            st.write(response)
            answers_dict[user_question] = details
            # print(answers_dict)
            save_answer(
                answers_dict,
                file_name=filename,
            )
            convert_json_to_md(file_name=filename)


def get_offset_by_name(name):
    if "information retrieval" in name:
        page_offset = -23
    elif "Datamining" in name:
        page_offset = -36
    elif "DWT" in name:
        page_offset = -12
    elif "Machine Learning" in name:
        page_offset = 1
    else:
        page_offset = 1
    return page_offset


if __name__ == "__main__":
    main()
