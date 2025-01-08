### Estimate the space usage of the Reuters-RCV1 dictionary with blocks of size k = 8 and k = 16 in
blocked dictionary storage.

With a block size of k = 8, we can estimate the space usage of the Reuters-RCV1 dictionary in blocked dictionary storage by using the formula given in the context:

400,000×(4+4+3+8)=7.6 MB

Thus, with a block size of k = 8, the space usage for the dictionary would be 7.6 MB.

Similarly, with a block size of k = 16, we can estimate the space usage as follows:

400,000×(4+4+3+8)=7.6 MB

Therefore, with a block size of k = 16, the space usage for the dictionary would also be 7.6 MB.
 - Source: [84, 86, 62, 74]


### Estimate the space usage of the Reuters-RCV1 dictionary with blocks of size k = 8 and k = 16 in
blocked dictionary storage
k=8: 400,000 * (4+4+3+8) = 7.6 MB
    k=16: 400,000 * (4+4+3+8) = 7.6 MB

 - Source: [109, 111, 87, 99]


### Compute the (tf x idf) weight for terms in documents d1-d5, in two ways:
tf = number of occurrencs of a term in a document
tf = number of occurrencs of a term in a document divided with the number of
occurrences of the term that occurs most frequently in the same document.
What kind of differences in weights you can find?
Assume that the user gives the query terms {computer want try}. Calculate cosine similarity
value for the five documents to find best match of the query.

The (tf x idf) weights for the terms in documents d1-d5 are:

Document 1:
- computer: 1.65 * 1 = 1.65
- want: 0 * 1 = 0
- try: 0 * 1 = 0

Document 2:
- computer: 1.65 * 2/2 = 1.65
- want: 0 * 2/2 = 0
- try: 0 * 2/2 = 0

Document 3:
- computer: 1.65 * 3/3 = 1.65
- want: 1.5 * 3/3 = 1.5
- try: 0 * 3/3 = 0

Document 4:
- computer: 1.65 * 4/4 = 1.65
- want: 0 * 4/4 = 0
- try: 1.5 * 4/4 = 1.5

Document 5:
- computer: 1.65 * 5/5 = 1.65
- want: 0 * 5/5 = 
 - Source: [109, 108, 116, 110]


### Suppose that a user’s initial query is cheap CDs cheap DVDs extremely cheap CDs. The
user examines two documents, d1 and d2. She judges d1, with the content CDs cheap
software cheap CDs relevant and d2 with content cheap thrills DVDs nonrelevant.
Assume that we are using direct term frequency (with no scaling and no document
frequency). There is no need to length- normalize vectors. Using Rocchio relevance
feedback (as specified in SMART Algorithm) what would the revised query vector be
after relevance feedback? Assume α = 1, β = 0.75, γ = 0.25.
The revised query vector would be:
⃗qm = (1 - 0.75)(1/3, 1/3, 0) + 0.75(1/2, 0, 1/2) - 0.25(0, 1/2, 0) = (0.1875, 0.375, 0.1875)
 - Source: [167, 166, 168, 169]


### Classify whether a given person is a male or a female based on the measured features. The
features include height, weight, and foot size. Data set is shown below
sex height (feet) weight (lbs) foot size
male 6 180 12
(inches)
male 5.92 (5'11") 190 11
male 5.58 (5'7") 170 12
male 5.92 (5'11") 165 10
female 5 100 6
female 5.5 (5'6") 150 8
female 5.42 (5'5") 130 7
female 5.75 (5'9") 150 9

This question cannot be answered based on the given context. The context does not mention any classification algorithm or model to determine whether a person is male or female based on the given features. Additionally, there is no information on the accuracy or effectiveness of the algorithm or model.
 - Source: [251, 255, 310, 311]


### Classify whether a given person is a male or a female based on the measured features. The
features include height, weight, and foot size. Data set is shown below
sex height (feet) weight (lbs) foot size
male 6 180 12
male 5.92 (5'11") 190 11
male 5.58 (5'7") 170 12
male 5.92 (5'11") 165 10
female 5 100 6
female 5.5 (5'6") 150 8
female 5.42 (5'5") 130 7
female 5.75 (5'9") 150 9

Below is a sample to be classified using Naive Bayes algorithm as a male or female.
sex height weight foot size
sample  6 130 8


Based on the given data set and the measured features of the sample, the person can be classified as a female. This is because the average height, weight, and foot size of females in the data set are closer to the sample's measurements compared to the average measurements of males. Additionally, the sample's foot size of 8 is exclusively found in females in the data set. Therefore, using the Naive Bayes algorithm, the sample can be classified as a female.
 - Source: [254, 251, 249, 308]


### Explain Random forest classification model. How is it differs from a
single decision tree in terms of bias, variance, and prediction accuracy

Random forest is a powerful classification model that combines the versatility of many decision tree models into a single model. It works by generating multiple decision trees, each using a subset of features and training data, and then using majority voting to make a final prediction. This ensemble model is gaining popularity among machine learning practitioners due to its superior results in solving a wide range of classification problems.

In terms of bias, random forest reduces bias by averaging the predictions of multiple decision trees, thereby reducing the chances of overfitting to the training data. In contrast, a single decision tree can have high bias if it is too simple and cannot capture the complexity of the data.

In terms of variance, the random forest model reduces the variance by creating multiple decision trees with different subsets of features and training data, thereby reducing the chances of overfitting to the training data. In contrast, a single decision tree can have high variance if it is too complex and is overfitting to the training data.

In terms of prediction accuracy, random forest generally outperforms a single decision tree because it combines the predictions of multiple decision trees, thereby reducing the chances of overfitting and improving the overall accuracy. However, in some cases, a single decision tree may perform better if the data is not complex enough
 - Source: [356, 714, 354, 355]


###  Data: A sample of 25 individuals is taken, and their cholesterol levels are
measured.
Cholesterol Levels (mg/dL): 205, 198, 210, 190, 215, 205, 200, 192, 198,
205, 198, 202, 208, 200, 205, 198, 205, 210, 192, 205, 198, 205, 210,
192, 205.
Define and test null- hypothesis.

Null hypothesis: The mean cholesterol level of the population is 200 mg/dL.

To test this null hypothesis, we can use a one-sample t-test. The t-test will compare the mean cholesterol level of our sample (205.68 mg/dL) to the hypothesized population mean (200 mg/dL). The t-statistic will be calculated using the formula: t = (sample mean - hypothesized mean) / (standard error). 

Using the given data, we can calculate the standard error as follows:

SE = √(variance / sample size) = √(38.36 / 25) = 1.96 

Therefore, the t-statistic can be calculated as: t = (205.68 - 200) / 1.96 = 2.86.

The degrees of freedom for this test will be n-1 = 24. Using a t-table, we can find the critical value for a two-tailed test at a significance level of 0.05 to be 2.064. Since the calculated t-statistic (2.86) is greater than the critical value (2.064), we reject the null hypothesis and conclude that the mean cholesterol level of the population is significantly different from
 - Source: [250, 248, 262, 94]


### Consider the following dataset. You are asked to split the data based on the
attribute Outlook. Calculate the Information Gain from splitting the
dataset on Outlook.
Outloo
k
Temperatu
re
Humidit
Wind
Play
y
y
Tennis
Sunny Hot High False No
Sunny Hot High True No
Overca
st Hot High False Yes
Rainy Mild High False Yes
Rainy Cool Normal False Yes
Sunny Cool Normal False Yes
The Information Gain for splitting the dataset on Outlook can be calculated by finding the entropy before and after the split.

Entropy before split = -(9/14)*log(9/14) - (5/14)*log(5/14) = 0.940

To calculate the entropy after the split, we need to consider the entropy for each partition and then take the weighted average.

For the partition where Outlook is 'Sunny', we have 2 instances of 'No' and 1 instance of 'Yes'. So, the entropy for this partition is -(2/3)*log(2/3) - (1/3)*log(1/3) = 0.918.

For the partition where Outlook is 'Overcast', we have 0 instances of 'No' and 1 instance of 'Yes'. So, the entropy for this partition is 0.

For the partition where Outlook is 'Rainy', we have 2 instances of 'No' and 2 instances of 'Yes'. So, the entropy for this partition is -(2/4)*log(2/4) - (2/4)*log(2/4) = 1.

Weighted average entropy after split = (3/14)*0
 - Source: [344, 298, 343, 348]


### What is the number of types, number of tokens and name the terms present in this verse.
Fischer’s Fritz fischt frische fische frische fische fische fischt der fritz
Use space for tokenization. Do not count lowercase and uppercase as different types


Number of types: 8
Number of tokens: 13
Terms present: Fischer, Fritz, fischt, frische, fische, der
 - Source: [21, 22, 23, -10]


### What is the number of types, number of tokens and name the terms present in this verse.
Fischer’s Fritz fischt frische fische frische fische fische fischt der fritz
Use space for tokenization. Do not count lowercase and uppercase as different types. 

Number of types: 9
Number of tokens: 14
Terms: Fischer, Fritz, fischt, frische, fische, der
 - Source: [21, 22, 23, 29]


### State and explain the pseudocode to construct an index for a large data corpus using single pass memory indexing concept.

1. Set up memory, disk, and time constraints for the system.
2. Create a data structure for storing the index, such as a hash table or a tree.
3. Begin reading the collection and assembling all term-docID pairs.
4. For each term-docID pair, check if the term is already in the data structure.
5. If the term is not in the data structure, add it and create a postings list for the docID.
6. If the term is already in the data structure, add the docID to its postings list.
7. Update statistics for each term, such as term frequency and document frequency.
8. Continue reading the collection until all term-docID pairs have been processed.
9. Once all pairs have been processed, the index is complete and can be used for retrieval.
10. If the collection is too large to fit in memory, use a two-pass approach where the vocabulary is compiled in the first pass and the inverted index is constructed in the second pass.
11. If the collection is dynamic, use a similar approach as in step 10 but with an auxiliary index for new documents.
12. For large collections, consider using MapReduce or other distributed algorithms for indexing in a computer cluster.
 - Source: [63, 61, 71, 75]


### single pass memory indexing concept.
Single-pass in-memory indexing is a method of constructing an index in which the entire collection is scanned only once, and the index is built in memory using a data structure called the dictionary. This allows for more efficient use of memory compared to other methods, such as blocked sort-based indexing, which require multiple passes through the collection. The process of single-pass in-memory indexing involves tokenizing the collection, adding terms and their corresponding document IDs to the dictionary, and periodically writing the dictionary and postings lists to disk. This method also utilizes compression techniques to further increase efficiency. 
 - Source: [63, 71, 77, 67]


### Explain the following evaluation metrics and give results for query Q1 for both systems.
Precision at rank 10.	[2 marks]
Recall at precision 0.5.

Precision at rank 10 is a measure of how well a system performs in retrieving relevant documents within the top 10 results. It is calculated by dividing the number of relevant documents retrieved in the top 10 results by 10. 

For example, if a system retrieves 6 relevant documents within the top 10 results, the precision at rank 10 would be 0.6 or 60%. 

For query Q1, we do not have enough information to calculate the precision at rank 10 for either system. We would need to know the number of relevant documents retrieved within the top 10 results for each system.

Recall at precision 0.5 is a measure of how well a system performs in retrieving relevant documents while maintaining a precision of 0.5. It is calculated by finding the recall value at which the precision is 0.5.

For example, if a system retrieves 10 relevant documents and 10 non-relevant documents, the recall at precision 0.5 would be 0.5 or 50%.

For query Q1, we do not have enough information to calculate the recall at precision 0.5 for either system. We would need to know the number of relevant and non-relevant documents retrieved for each system
 - Source: [147, 142, 144, 145]


### Illustrate the step that map a term into four-character form.

The step that maps a term into four-character form is called normalization, which is one of the steps performed during tokenization. This step involves converting each term into its base form, discarding any variations or punctuation, and then padding the remaining characters with trailing zeros. For example, the term 'friends' would be normalized as 'F653'.
 - Source: [59, 29, 21, 69]


### Describe the difference between relevance feedback and query expansion in terms of user interaction.

Relevance feedback involves explicit interaction from the user, where they are asked to provide feedback on the relevance of retrieved documents. This feedback is then used to improve future retrieval results. On the other hand, query expansion does not require explicit interaction from the user. Instead, it uses techniques such as pseudo relevance feedback to automatically analyze the user's initial query and expand it to include additional terms or concepts that may improve the relevance of retrieved documents. This method does not require any extended interaction with the user.
 - Source: [170, 395, 169, 171]


### The following list of Rs and Ns represent relevant (R) and non-relevant (N) returned
documents in a ranked list of 10 documents retrieved in response to a query from a collection of
1000 documents. The top of the ranked list is on the left of the list. The list show 4 relevant
documents. Assume that there are 6 relevant documents in the collection.
R R N N N R N R N
Calculate the R-precision of the system?
The R-precision of the system is 2/6 = 0.3333 or 33.33%.
 - Source: [143, 142, 151, 150]


### Given data [21, 24, 25, 26, 28, 29, 34, 4, 8, 9, 15, 21]
Create bins using equal frequency approach with bin frequency
4. Perform smoothing by bin means and bin boundaries.

Bins: Bin 1: 4, 8, 9, 15
      Bin 2: 21, 21, 24, 25
      Bin 3: 26, 28, 29, 34

Smoothing by bin means: 
Bin 1: 9, 9, 9, 9
Bin 2: 22.75, 22.75, 22.75, 22.75
Bin 3: 29.25, 29.25, 29.25, 29.25

Smoothing by bin boundaries:
Bin 1: 4, 4, 9, 15
Bin 2: 21, 21, 24, 25
Bin 3: 26, 26, 34, 34
 - Source: [107, 90, 89, 80]


### Q13. Suppose a group of 12 sales price records has been sorted as follows:
5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215.
Partition them into three bins by each of the following methods.
(a) Equal-frequency (equidepth) partitioning
(b) Equal-width partitioning
(c) Clustering

(a) Equal-frequency (equidepth) partitioning:
Bin 1: 5, 10, 11, 13, 15
Bin 2: 35, 50, 55, 72, 92
Bin 3: 204, 215

(b) Equal-width partitioning:
Bin 1: 5, 10, 11, 13, 15
Bin 2: 35, 50, 55, 72, 92
Bin 3: 204, 215

(c) Clustering:
Bin 1: 5, 10, 11, 13, 15
Bin 2: 35, 50, 55
Bin 3: 72, 92, 204, 215
 - Source: [107, 116, 90, 54]


### In the first 5 days of the week the number of customers
visited are 50,60,40,47,53. The expected percentage of customer
to visit the shop is uniform in everyday. Find out the Pearson Chi-
square(Lambda^2) value for the given data.

16.6
 - Source: [55, 95, 54, 53]


### What is dying ReLu Problem? Explain with example.

    The dying ReLU problem refers to a situation where a ReLU neuron becomes inactive and outputs zero for all inputs. This can cause problems in the neural network, as the neuron will no longer contribute to the overall computation. This can happen if the weights and biases of the neuron are not set properly during training, causing the neuron to always output negative values. For example, a ReLU neuron with a weight of -1 and a bias of 0 will always output 0, regardless of the input. This can be problematic because it limits the network's ability to learn and can lead to lower accuracy.
 - Source: [29, 18, 32, 27]


### What is dropout and batch normalization?

Dropout is a method for preventing overfitting in deep neural networks. It is implemented by randomly deactivating neurons during training, forcing the network to be accurate even in the absence of certain information. This prevents the network from becoming too dependent on any one or small combination of neurons. 

Batch normalization is a technique used to accelerate the training of neural networks. It addresses the issue of unstable output distributions in the lower layers of the network by normalizing the distribution of outputs at each layer. This significantly speeds up training and allows for more layers to be added to the network without sacrificing performance.
 - Source: [50, 118, 124, 51]


