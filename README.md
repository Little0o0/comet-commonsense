# COMET based on ATOMIC and ENet

> This repository is only used for 2020 Summer Research - Encyclopedia Net.

To run a generation experiment (either conceptnet or atomic), follow these instructions:

<h1>First Steps</h1>

First clone, the repo:

```
git clone https://github.com/Little0o0/comet-commonsense.git
```

Then run the setup scripts to acquire the pretrained model files from OpenAI, as well as the ATOMIC and ENet datasets

For Atomic dataset
```
bash scripts/setup/get_atomic_data.sh]
```

For ENet dataset
You can just put the File into the data/ENet (current)


Then install dependencies (assuming you already have Python 3.6 and Pytorch >= 1.0:

```
pip install tensorflow
pip install ftfy==5.1
conda install -c conda-forge spacy
python -m spacy download en
pip install tensorboardX
pip install tqdm
pip install pandas
pip install ipython
```
<h1> Making the Data Loaders </h1>

Run the following scripts to pre-initialize a data loader for ATOMIC and ENet:

```
python scripts/data/make_atomic_and_ENet_data_loader.py
```

For the ATOMIC KG, if you'd like to make a data loader for only a subset of the relation types, comment out any relations in lines 17-25. 

For ConceptNet if you'd like to map the relations to natural language analogues, set ```opt.data.rel = "language"``` in line 26. If you want to initialize unpretrained relation tokens, set ```opt.data.rel = "relation"```

<h1> Setting the ATOMIC configuration files </h1>

Open ```config/atomic/changes.json``` and set which categories you want to train, as well as any other details you find important. Check ```src/data/config.py``` for a description of different options. Variables you may want to change: batch_size, learning_rate, categories. See ```config/default.json``` and ```config/atomic/default.json``` for default settings of some of these variables.


<h1> Running the ATOMIC and ENet experiment </h1>

<h3> Training </h3>
For whichever experiment # you set in ```config/atomic/changes.json``` (e.g., 0, 1, 2, etc.), run:

```
python src/main.py --experiment_num #
```

<h3> Evaluation </h3>

Once you've trained a model, run the evaluation script:

```
python scripts/evaluate/evaluate_generation_model.py --split $DATASET_SPLIT --model_name /path/to/model/file
```

<h3> Generation </h3>

Once you've trained a model, run the generation script for the type of decoding you'd like to do:

```
python scripts/generate/generate_beam_search.py --beam 10 --split $DATASET_SPLIT --model_name /path/to/model/file
python scripts/generate/generate_greedy.py --split $DATASET_SPLIT --model_name /path/to/model/file
python scripts/generate/generate_topk.py --k 10 --split $DATASET_SPLIT --model_name /path/to/model/file
```
