import BN_helper
import CBN_model
from DunGen_BN import model as inference_model
from CBN_node_classes import Size, Entrance, Boss, Exit, Empty, Treasure, Trap, Adjacency

structured_model = CBN_model.DAG([Treasure(1), Treasure(2), Trap(1), Trap(2), Empty(1), Empty(2)])

input_size = input("s, m, or l? ")
if input_size not in ["s", "m", "l"]:
    raise ValueError("Input must be 's', 'm', or 'l'.")

given = {'size': str.strip(input_size)}
parameters = BN_helper.decorate(inference_model.predict_proba(given))

structured_model.populate_and_orient(parameters) # generate nodes and populate with parameters
# structured_model.cascade_inference() # make cascading decisions through the BN
# structured_model.write("all")

print(parameters)
