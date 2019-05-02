from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.utils import EndpointConfig
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.fallback import FallbackPolicy

if __name__ == '__main__':
	logging.basicConfig(level='INFO')
	training_data_file = './data/stories.md'
	model_path = './models/dialogue'
	domain_file = "CSRBot_domain.yml"
	nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/csrbotnlu')

	action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")

	fallback = FallbackPolicy(fallback_action_name="action_default_fallback", core_threshold=0.3, nlu_threshold=0.3)

	agent = Agent(domain_file,
				  policies=[MemoizationPolicy(max_history=2), KerasPolicy(max_history=3, epochs=3, batch_size=50),fallback],
				  interpreter=nlu_interpreter,action_endpoint=action_endpoint)

	agent.train(agent.load_data(training_data_file))
	agent.persist(model_path)
	#agent.visualize(training_data_file,output_file="graph1.png", max_history=3)


