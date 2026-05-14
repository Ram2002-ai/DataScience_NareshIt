import torch
from transformers import BertTokenizer,BertForSequenceClassification,Trainer,TrainingArguments
from datasets import load_dataset
from pydantic import BaseModel
import streamlit as st
import requests


# load the pre-trained BERT model and tokenizer

tokenizer=BertTokenizer.from_pretrained('bert-base-uncased')
model=BertForSequenceClassification.from_pretrained('bert-base-uncased',num_labels=2)

# load the imdb dataset

dataset=load_dataset('imdb')

# tokenize the dataset

def tokenize_function(example):
    return tokenize_function(example['text'],padding='max_length',truncation=True)

# Apply the tokenization function to the dataset
tokenize_datasets=dataset.map(tokenize_function,batched=True)


# Define training arguments
traing_args=TrainingArguments(
    output_dir='./results',
    evaluation_strategy='epoch',
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10
)

# initialize the trainer
trainer=Trainer(
    model=model,
    args=traing_args,
    train_dataset=tokenize_datasets['train'],
    eval_dataset=tokenize_datasets['test']
)

# start the training process
trainer.train()

# after fine-tuning use the model for predictions
inputs=tokenizer('I love this product!','This is terrible,do not buy it',padding=True,truncation=True,return_tensors='pt')

# ensure model is in evaluation mode
model.eval()

# move inputs and model to the same device
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)
inputs=inputs.to(device)

# get predictions
with torch.no_grad():
    outputs=model(**inputs)
    logits=outputs.logits

# convert logits to probabilities
probs=torch.nn.functional.softmax(logits,dim=-1)

# get predicted class (0or 1 for binary classification)
predictions=torch.argmax(probs,dim=-1)
print(predictions)

# evaluate the model on the test set
eval_results=trainer.evaluate()
print(eval_results)

