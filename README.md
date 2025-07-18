# Comment-Filtering-using-LSTM-LLama-guard

Data Upload:
 Changed from using pwd to using os.path.join method to load up the dataset; helped with shortcutting the code.
 Learned Llama BasicModelRunner which just loads models from huggingface.
 Learned about huggingface’s dataset library which has load_model which has a streaming parameter to stream huge datasets online.
Preprocessing:
 Faced the problem with concatenating the two column dataframe into one to then perform the tokenization.
 Used the prompt_template to concate the two columns together; another solution would be to change the two columns to strings and concatinate them by running a for loop over the range of their column lengths.
 Specified the returned tensor to match the input type for the data required by the model; also to specify the max_length for padding.
 Learned about fine-tuning and prompt engineering.
 Learned about Auto-tokenizer which is a library from transformers to specify which tokenizer to use for a specific model.
 Learned that every model has its own tokenizer.
 Learned about padding and truncation which are two methods to perform after tokenization.
 Had to set the max_length padding to ensure that the total length needed for the variables is the same for each variable and to not exceed a specific number.
 First I wanted to use tfidf or bow to tokenize then figured keras.layers TextVectorizer would work but it was specific
for a base-deep learning neural network; so the optimal was using the DistilBERT tokenizer as we’re going to use this model.
Model Configuration:
 Had a problem with the accelerator version and had to install the latest version for it to work.
 Had a problem with the model’s not able to read the data labels at it was strings not ints; had to perform a mapping label2id to fix it.
