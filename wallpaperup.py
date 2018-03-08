import argparse as ap
from WallpaperExtractor import WallpaperExtractor

parser = ap.ArgumentParser()
parser.add_argument("keyword", type=str, help="Pass a keyword to be searched for.")
parser.add_argument("-s", "--save", dest='s', type=str, help="Saving location.")
parser.add_argument("-r", "--random", dest='r', action="store_true", help="To download any random wallpaper related to keyword.")
parser.add_argument("--onpage", type=int, dest='p', help="All images on a page related to keyword.")
parser.add_argument("-a", "--all", action="store_true", dest='a', help="To download every possible image related to keyword.")
args = parser.parse_args()

if args.r and args.p and args.s and not args.a:
    downloader = WallpaperExtractor.WallpaperUp(args.keyword)
    downloader.random_download(args.s, args.p)
elif args.p and not args.r and not args.a and args.s:
    downloader = WallpaperExtractor.WallpaperUp(args.keyword)
    downloader.download_single_page(args.s, args.p)
elif args.a and args.s:
    num_of_pages=int(input("[Number of Pages to Scrape]: "))
    downloader = WallpaperExtractor.WallpaperUp(args.keyword)
    downloader.downloadAllImages(args.s, num_of_pages)
else:
    print("Wrong arguments passed!!")
