# ml_project_image_cap

## usage

- only refine the caption json file

  ```bash
  python translate.py --refine <path/to/raw/captions.json>
  ```

- refine and then translate the caption json file

  ```bash
  python translate.py --refine --translate <path/to/raw/captions.json>
  ```

- translate already refined caption json file

  ```bash
  python translate.py --translate <path/to/refined/captions.json>
  ```
