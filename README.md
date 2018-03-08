# Wallpaper Downloader

A simple **Wallpaper Scraper** which will enable you to download as many wallpapers as you want without any problem.

## Getting Started
These instructions will get you a copy of the program.

### Installing
Just clone this repository. The main executable file is ```wallpaperup.py```.

### Requirements
To install all the requirements, do the following;
```
pip install requirements.txt
```
### Examples
1. To download a random wallpaper related to the keyword.
```
python3.5 wallpaperup.py <keyword> -r -s <saving_location> --onpage <page_number>
```
2. To download all the images on a page.
```
python3.5 walllpaperup.py <keyword> --onpage <page_number> -s <saving_location>
```
3. To download all the images from page 1 to specified page number.
```
python3.5 wallpaperup.py <keyword> --all --onpage <page_number> -s <saving_location>
```

## Built with
1. Requests
2. BS4

## Author
Himanshu Sharma
