import markdown
import sys
from jinja2 import Environment, FileSystemLoader

def main() :
    f = sys.argv[1]
    done = False
    slides = []
    with open(f, 'r') as fil :
        while not done:
            current_page = []
            while True :
                l = fil.readline()
                if(l.startswith("---")):
                    break
                if(l==''  ):
                    done = True
                    break
                current_page.append(l)
            hml = markdown.markdown("\n".join(current_page))
            slides.append(hml)

    env = Environment(loader=FileSystemLoader("."))
    tmplt = env.get_template("slides.html")
    with open("out.html",'w') as out :
        out.write(tmplt.render(slides=slides))
        

if __name__ == "__main__":
    main()
