from django.db import models
import json

# Create your models here.
class Challenge(models.Model):
    json_items = models.CharField(max_length=200)
    json_result = models.CharField(max_length=200)

    def evaluate_array(**kwargs):
        new_array = []
        for key, value in kwargs.items():
            if key == 'items':
                for i in value:
                    if type(i)==int:
                        new_array.append(i)
                    else:
                        for val in i:
                            if type(val)==int:
                                new_array.append(val)
                            else:
                                for row in val:
                                    new_array.append(row)
          
        json_result = {"result":new_array}    
        return json_result
    
    def assign(self):
        self.json_result = evaluate_array(json.loads(self.json_items))