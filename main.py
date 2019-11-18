#%%
import json
from EDA.eda_project_a import binary_plot
from Feature_Creation.feature_project_a import func_1,func_2


if __name__ == "__main__":
    with open('config.json') as json_file:
        config = json.load(json_file)
    A = config['EDA_var']['Column1']
    B = config['EDA_var']['Column2']
    print(A)
    print(B)
    binary_plot(A,B)
    func_1()
    func_2()
    

# %%
