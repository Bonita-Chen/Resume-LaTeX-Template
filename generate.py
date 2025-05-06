import yaml
from jinja2 import Environment, FileSystemLoader

def main():
    # 1) 读取用户数据
    with open("data.yaml", "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # 2) 渲染 LaTeX 模板
    env = Environment(
        loader=FileSystemLoader("."),
        block_start_string="{%",
        block_end_string="%}",
        variable_start_string="{{",
        variable_end_string="}}",
        autoescape=False
    )
    template = env.get_template("template.tex")
    rendered = template.render(**data)

    # 3) 输出 main.tex
    with open("main.tex", "w", encoding="utf-8") as f:
        f.write(rendered)

if __name__ == "__main__":
    main()
