from base64 import b64encode

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.statemachine import StringList
from sphinx.util.docutils import SphinxDirective
from sphinx.util.osutil import relative_uri, canon_path

from sphinx.util import logging

logger = logging.getLogger(__name__)


class pyrobotsim(nodes.Element, nodes.General):
    pass


def visit_pyrobotsim_html(self, node):
    tag = self.starttag(node, "div", CLASS="pyrobotsim")
    self.body.append(tag.strip())

    base64_code = b64encode(node["code"].encode("UTF-8")).decode("UTF-8")

    options = set(PyRobotSim.option_spec.keys()).difference(
        ["code", "scrollx", "scrolly", "extra_args", "showtitle"]
    )

    query_args = {k: node[k] for k in options}
    query_args["main"] = base64_code
    query_args["scrollX"] = node['scrollx']
    query_args["scrollY"] = node['scrolly']

    width = node["width"]
    height = node["height"]
    left_shift = 0

    if "%" in width:
        width_percent = float(width.split("%")[0])
        left_shift = (width_percent - 100) / 2
        
        

    # logger.info(f"extra args: {node['extra_args']}")

    for arg, value in node["extra_args"].items():
        query_args[arg] = value



    query_string = "&".join([f"{k}={v}" for k, v in query_args.items()])

    #logger.info(f"Query args: {query_args}")
    #logger.info(f"Query string: {query_string}")

    url = f'''{node["pyrobotsim_root_url"]}?{query_string}'''
    self.body.append(f'''<a target="_blank" href="{url}">{node["showtitle"]}</a>''')
    self.body.append(f'''
        <iframe src="{url}"
            class="pyrobotsim-frame"
            frameborder="0"
            border="0"
            cellspacing="0"
            width="{width}"
            height="{height}"
            style="resize:both; position:relative; left:-{left_shift}%"
        >'''
    )


def depart_pyrobotsim_html(self, node):
    self.body.append("</iframe>")
    self.body.append("</div>")


def visit_pyrobotsim_latex(self, node):
    self.body.append("\\begin{lstlisting}\n")
    self.body.append(node["code"].strip())


def depart_pyrobotsim_latex(self, node):
    self.body.append("\n \\end{lstlisting}")

def parse_extra_args(argument):
    pairs = [x.strip().split('=') for x in argument.strip().split('&')]
    return {arg.strip(): value.strip() for arg, value in pairs}
    
def parse_files(argument):
    return argument.replace(' ', '')



class PyRobotSim(SphinxDirective):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "world": directives.unchanged,
        "vsplit": directives.nonnegative_int,
        "hsplit": directives.nonnegative_int,
        "zoom": int,
        "x": int,
        "y": int,
        "angle": int,
        "scrollx": int,
        "scrolly": int,
        "camera": lambda arg: directives.choice(arg, ("free", "follow")),
        "height": directives.length_or_percentage_or_unitless,
        "width": directives.length_or_percentage_or_unitless,
        "extra_args": parse_extra_args,
        "showtitle": directives.unchanged,
        "files": parse_files
    }
    has_content = True


    def run(self):
        def get_option(opt_name, default_value):
            return opt_name in self.options and self.options[opt_name] or default_value

        self.assert_has_content()
        pyrobotsim_root_url = self.env.config.pyrobotsim_root_url

        code_lines = self.content
        code = "\n".join(code_lines)
        default_height = "700px"

        container = pyrobotsim(
            "",
            code=code,
            world=get_option("world", "emptyWorld"),
            vsplit=get_option("vsplit", 35),
            hsplit=get_option("hsplit", 600),
            zoom=get_option("zoom", 0),
            x=get_option("x", 0),
            y=get_option("y", 0),
            angle=get_option("angle", 0),
            scrollx=get_option("scrollx", 0),
            scrolly=get_option("scrolly", 0),
            camera=get_option("camera", "free"),
            width=get_option("width", "110%"),
            height=get_option("height", self.env.config.pyrobotsim_height),
            extra_args=get_option("extra_args", {}),
            showtitle=get_option("showtitle", "Show in separate window"),
            files=get_option("files", []),
            pyrobotsim_root_url=pyrobotsim_root_url,
        )
        self.set_source_info(container)

        return [container]


def setup(app):
    app.add_config_value(
        "pyrobotsim_root_url",
        "https://21learning-components.surge.sh/#/component/PyRobotSim",
        "html",
    )
    app.add_config_value(
        "pyrobotsim_height",
        "600px",
        "html",
    )
    app.add_directive("pyrobotsim", PyRobotSim)
    app.add_node(
        pyrobotsim,
        html=(visit_pyrobotsim_html, depart_pyrobotsim_html),
        latex=(visit_pyrobotsim_latex, depart_pyrobotsim_latex),
    )
