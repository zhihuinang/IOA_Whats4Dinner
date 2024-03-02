import json
import os

restaurant_json = "./restaurant.json"
grade_urls = [
    "/restaurant/所内食堂/", "/restaurant/融科-计算所沿线/",
    "/restaurant/中关村5号/", "/restaurant/融科以及融科西侧沿线/",
    "/restaurant/青年公寓附近/", "/restaurant/其他附近餐厅/"
]
grade_dirs = ["." + x for x in grade_urls]

for x in grade_dirs:
    os.makedirs(x,exist_ok=True)

course_page_template = """
# {restaurant_name}

本页面暂无内容，期待大家的共同建设

### 基本评价
- 口味
- 价格

### 个人评价
等待你的信息与观点
"""

entry_template = "- [{restaurant_name}]({grade_url}{restaurant_name})\n"


with open(restaurant_json, encoding="utf8") as f:
    restaurant = json.load(f)

# basic data validation
assert len(restaurant) == 6
assert all(isinstance(x, dict) for x in restaurant)

for i in range(6):
    grade_restaurant, grade_dir, grade_url = restaurant[i], grade_dirs[i], grade_urls[i]
    readme = open(os.path.join(grade_dir, "README.md"),
                  mode="a", encoding="utf8")
    sidebar = open(os.path.join(grade_dir, "_sidebar.md"),
                   mode="a", encoding="utf8")
    for course_id in sorted(grade_restaurant.keys()):  # sort by course ID
        course_name = grade_restaurant[course_id]
        course_path = os.path.join(
            grade_dir, course_name + ".md")
        if not os.path.exists(course_path):
            with open(course_path, "w", encoding='utf8') as page:
                page.write(course_page_template.format(
                    restaurant_name=course_name)
                )
        readme.write(entry_template.format(
            restaurant_name=course_name, grade_url=grade_url
        ))
        sidebar.write(entry_template.format(
            restaurant_name=course_name, grade_url=grade_url
        ))
