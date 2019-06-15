from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, configs, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(configs))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'sell4bidsbotnlu')
	
def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/sell4bidsbotnlu')
	print(interpreter.parse(u"How it works for sellers"))
	print(interpreter.parse(u"what can be bought sold here"))
	print(interpreter.parse(u"have a good day").get('intent'))
	
if __name__ == '__main__':
	train_nlu('./data/nlu_traning_faq.md', 'config_spacy.json', './models/nlu')
	#train_nlu('./data/data1.json', 'config_spacy.json', './models/nlu')
	#train_nlu('./data/nlu_data.md', 'config_spacy.json', './models/nlu')
	run_nlu()
