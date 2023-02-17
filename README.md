# ml_project_image_cap

translation of image caption dataset into bengali

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

## example

```json
{
  "id": 86220,
  "file_name": "000000086220.jpg",
  "captions": [
    "A car and a public transit vehicle on a road.",
    "a car in front of a train on train tracks",
    "A tram and a car make their way through town.",
    "A silver car in the street next to a metal railing.",
    "A white car and a white bus parked parallel from one another. "
  ]
}
```

[![86220](assets/000000086220.jpg)](http://images.cocodataset.org/val2017/000000086220.jpg)

```json
{
  "id": 86220,
  "file_name": "000000086220.jpg",
  "captions": [
    "একটি রাস্তায় একটি গাড়ি এবং একটি পাবলিক ট্রানজিট যান।",
    "ট্রেনের ট্র্যাকে একটি ট্রেনের সামনে একটি গাড়ি",
    "একটি ট্রাম এবং একটি গাড়ি শহরের মধ্য দিয়ে যায়৷",
    "ধাতব রেলিংয়ের পাশে রাস্তায় একটি সিলভার গাড়ি।",
    "একটি সাদা গাড়ি এবং একটি সাদা বাস একে অপরের থেকে সমান্তরালভাবে দাঁড়িয়ে আছে।"
  ]
}
```
