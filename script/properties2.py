import json

from bs4 import BeautifulSoup

# The given HTML table
html_content = """
<table class="tablelist responsive-table">
    <tbody>
        <tr>
            <th rowspan="3">地物情報</th>
            <th>地物名</th>
            <th>説明</th>
            <th>属性の型</th>
        </tr>
        <tr>
            <td>土砂災害警戒区域（面）</td>
            <td>土砂災害警戒区域の範囲</td>
            <td>面型（GM_Surface）</td>
        </tr>
        <tr>
            <td>土砂災害警戒区域（線）</td>
            <td>土砂災害警戒区域の形状</td>
            <td>線型（GM_Curve）</td>
        </tr>
        <tr>
            <th rowspan="9">属性情報</th>
            <th>属性名<br>（かっこ内はshp属性名）</th>
            <th>説明</th>
            <th>属性の型</th>
        </tr>
        <tr>
            <td>現象の種類<br>（A33_001）</td>
            <td>土砂災害警戒区域の現象の種類</td>
            <td>コードリスト「<a href="/ksj/gml/codelist/CodeOfPhenomenon.html" target="_blank">現象種別コード</a>」</td>
        </tr>
        <tr>
            <td>区域区分<br>（A33_002）</td>
            <td>土砂災害警戒区域の指定の種類</td>
            <td>コードリスト「<a href="/ksj/gml/codelist/CodeOfZone_A33.html" target="_blank">区域コード</a>」</td>
        </tr>
        <tr>
            <td>都道府県コード<br>（A33_003）</td>
            <td>土砂災害警戒区域を指定した都道府県</td>
            <td>コードリスト「<a href="/ksj/gml/codelist/PrefCd.html" target="_blank">都道府県コード</a>」</td>
        </tr>
        <tr>
            <td>区域番号<br>（A33_004）</td>
            <td>土砂災害警戒区域の区域番号</td>
            <td>文字列型（CharacterString）</td>
        </tr>
        <tr>
            <td>区域名<br>（A33_005）</td>
            <td>土砂災害警戒区域の区域の名称</td>
            <td>文字列型（CharacterString）</td>
        </tr>
        <tr>
            <td>所在地<br>（A33_006）</td>
            <td>土砂災害警戒区域の位置する地名</td>
            <td>文字列型（CharacterString）</td>
        </tr>
        <tr>
            <td>公示日<br>（A33_007）</td>
            <td>土砂災害警戒区域を公示した年月日</td>
            <td>日付型（TM_Period）</td>
        </tr>
        <tr>
            <td>特別警戒未指定フラグ<br>（A33_008）</td>
            <td>土砂災害警戒区域（イエローゾーン）のみ公示を行っているが、土砂災害特別警戒区域（レッドゾーン）の調査・公示を行っていない区域を示すフラグ </td>
            <td>コードリスト「<a href="/ksj/gml/codelist/CodeOfUnSpecification.html" target="_blank">特別警戒区域未指定コード</a>」</td>
        </tr>
    </tbody>
</table>
"""

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Extract the relevant data
data = {}
rows = soup.select("tr")

# Iterate over each relevant row, starting from the row containing the attributes
for row in rows:
    cells = row.find_all("td")
    if len(cells) > 0:
        # Extract key from the text inside parentheses
        key = cells[0].get_text(strip=True).split("（")[-1].rstrip("）")
        # Extract value before parentheses
        value = cells[0].get_text(strip=True).split("（")[0]
        data[key] = value

# Converting the result to JSON format
json_output = json.dumps(data, ensure_ascii=False, indent=4)
json_output

# ファイルの書き出し
with open("_properties.json", "w") as f:
    f.write(json_output)
