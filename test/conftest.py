import pytest 
from easy_serve import EasyServe

@pytest.fixture
def get_model():
    class TestModel(EasyServe):
        def __init__(self , param1:int):
            self.param1 = param1
        
        def model_init(self): 
            pass
            
        def preprocessing(self, request):
            return request.json['data']
        
        def inference(self, args):
            return f"{args} {self.param1}"
        
        def postprocessing(self , model_output):
            return f"Output: {model_output}"
        
    return TestModel