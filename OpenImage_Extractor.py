import fiftyone as fo
fo.config.dataset_zoo_dir = "./Dataset"
fo.zoo.load_zoo_dataset(
              "open-images-v7",
              split="train",
              label_types=["classifications"],
              classes=["Taco","Hot dog"],
              max_samples=3000,
          )
