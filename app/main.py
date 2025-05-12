
import sys
import pandas as pd
from PIL import Image
from utils import preprocess, predict, load_model

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import absl.logging
absl.logging.set_verbosity(absl.logging.ERROR)



def main(img_path):
    model = load_model("app/custom_model.h5")
    img = Image.open(img_path)
    input_tensor = preprocess(img)
    result, precision = predict(model, input_tensor)
    print(result, precision)

    output = {
        "image": os.path.splitext(os.path.basename(img_path))[0],
        "prediction": result,
        "precision": precision
    }
    df = pd.DataFrame([output])
    output_path = "/data/results.csv"
    df.to_csv(output_path, mode='a', index=False, header=not os.path.exists(output_path))


if __name__ == "__main__":
    main(sys.argv[1])