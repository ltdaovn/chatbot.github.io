import wikipedia as wiki
import sys
wiki.set_lang('vi')
def run(value):
	search = wiki.search(value)
	page = wiki.page(search[0])
	return str(page.summary)
def main():
	if len(sys.argv) > 1:
		print(run(sys.argv[1]))
main()		