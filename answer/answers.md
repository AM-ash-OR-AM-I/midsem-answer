### Write the pseudocode for Block sort based indexing method.

1. Start with a collection of documents
2. Set the variable n to 0
3. While all documents have not been processed:
    a. Increase n by 1
    b. Parse the next block of documents and assign it to the variable block
    c. Use the BSBI-Invert function to create an inverted index for the block
    d. Write the inverted index to disk with block number n
4. Once all blocks have been processed, merge the inverted indexes from each block into one large merged index
    a. Open all block files and maintain read buffers for each block and a write buffer for the merged index
    b. In each iteration, select the lowest termID that has not been processed yet using a priority queue
    c. Read the postings lists for this termID from each block and merge them
    d. Write the merged list back to disk
    e. Refill the read buffers when necessary
5. Calculate the total index construction time by adding the time for each step:
    a. Time for reading the collection
    b. Time for initial sorting of 10 records for each block
    c. Time for writing 10 blocks to disk
    d. Time for merging the
 - Source: [65, 75, 66, 63]


