import fiftyone as fo

fo.zoo.load_zoo_dataset(
              "open-images-v7",
              split="train",
              label_types=["classifications"],
              classes=["Taco", "Hot dog"],
              max_samples=100,
          )
