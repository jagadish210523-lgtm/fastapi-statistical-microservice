from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel, Field
from math import sqrt
jaga = FastAPI()


# Creating a Pydantic model called DatasetInput

class DatasetInput(BaseModel):
    dataset_name : str = "hi"
    values : List[float] = Field(min_length = 2, description = "Must need 2 numerical values")


@jaga.post("/analytics/spread")
async def calculate_spread(data : DatasetInput):
    nums = data.values
    count = len(nums)
    mean_val = sum(nums)/count
    variance = sum((x - mean_val) **2 for x in nums)/count
    std_deviation = sqrt(variance)
    return{
        "dataset_name" : data.dataset_name,
        "metrics" : {
            "variance" : round(variance,4),
            "standard_deviation" : round(std_deviation,4)
        }
    }
