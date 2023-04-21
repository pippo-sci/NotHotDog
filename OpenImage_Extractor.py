import fiftyone as fo
fo.config.dataset_zoo_dir = "./Dataset"
fo.zoo.load_zoo_dataset(
              "open-images-v7",
              split="train",
              label_types=["classifications"],
              classes=["Dog","Taco","Hot dog"],
              shuffle=True,
              max_samples=3000,
          )
