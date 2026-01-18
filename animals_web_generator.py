import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def print_animals():
    animals_data = load_data("animals_data.json")
    output = ""
    for animal in animals_data:
        output += '<li class="cards__item">'
        output += f'<div class="card__title">Name: {animal["name"]}<br/></div>\n'
        output += '<p class="card__text">'
        output += f"<strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n"
        output += f"<strong>Location</strong>: {animal["locations"][0]}<br/>\n"
        if "type" in animal.get("characteristics", {}):
            output += f"<strong>Type</strong>: {animal["characteristics"]["type"]}<br/>\n"
        output += '</p>'
        output += '</li>'
    return output


def load_html():
  """ Loads a html file """
  with open("animals_template.html", "r") as fileobj:
      return fileobj.read()


def replace_info(html):
    animals_info = print_animals()
    return html.replace("__REPLACE_ANIMALS_INFO__", animals_info)

def write_html(data):
    with open("animals.html", "w") as fileobj:
        fileobj.write(data)

def main():
    html = load_html()
    new_html = replace_info(html)
    write_html(new_html)


if __name__ == "__main__":
    main()