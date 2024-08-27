import json

from bs4 import BeautifulSoup

# The given HTML table
html_content = """
<tr>
										<td>小班ID<br>(A45_001)</td>
										<td>小班の識別子</td>
										<td>文字列型（CharacterString）</td>
									</tr>
									<tr>
										<td>森林管理局<br>(A45_002)</td>
										<td>当該小班を管轄する森林管理局の識別コード</td>
										<td>コードリスト「<a href="/ksj/gml/codelist/shinrinkanriCd.html" target="_blank">森林管理局コード</a>」</td>
									</tr>
									<tr>
										<td>森林管理署<br>(A45_003)</td>
										<td>当該小班を管轄する森林管理署の識別コード</td>
										<td>コードリスト「<a href="/ksj/gml/codelist/shinrinkanriCd.html" target="_blank">森林管理署コード</a>」</td>
									</tr>
									<tr>
										<td>林班主番<br>(A45_004)</td>
										<td>当該小班が所在する林班の番号</td>
										<td>整数型（Integer）</td>
									</tr>
									<tr>
										<td>林班枝番<br>(A45_005)</td>
										<td>当該小班が所在する林班の枝番</td>
										<td>整数型（Integer）</td>
									</tr>
									<tr>
										<td>小班主番<br>(A45_006)</td>
										<td>当該小班の識別コード</td>
										<td>コードリスト「<a href="/ksj/gml/codelist/shouhanshubanCd.html" target="_blank">小班主番コード</a>」</td>
									</tr>
									<tr>
										<td>小班枝番<br>(A45_007)</td>
										<td>当該小班の枝番</td>
										<td>整数型（Integer）</td>
									</tr>
									<tr>
										<td>局名称<br>(A45_008)</td>
										<td>当該小班を管轄する森林管理局の名称</td>
										<td>コードリスト「<a href="/ksj/gml/codelist/shinrinkanriCd.html" target="_blank">局名称コード</a>」</td>
									</tr>
									<tr>
										<td>署名称<br>(A45_009)</td>
										<td>当該小班を管轄する森林管理署の名称</td>
										<td>コードリスト「<a href="/ksj/gml/codelist/shinrinkanriCd.html" target="_blank">署名称コード</a>」</td>
									</tr>
									<tr>
										<td>小班名称<br>(A45_010)</td>
										<td>当該小班の名称</td>
										<td>文字列型（CharacterString）</td>
									</tr>
									<tr>
										<td>林小班名称<br>(A45_011)</td>
										<td>林班主番、林班枝番及び小班名称の組み合わせによる識別名</td>
										<td>文字列型（CharacterString）</td>
									</tr>
									<tr>
										<td>材積<br>(A45_012)</td>
										<td>当該小班の材積（森林の蓄積）。単位はm3とする</td>
										<td>整数型（Integer）</td>
									</tr>
									<tr>
										<td>国有林名称<br>(A45_013)</td>
										<td>当該小班が所在する国有林の名称</td>
										<td>文字列型（CharacterString）</td>
									</tr>
									<tr>
										<td>県市町村名称<br>(A45_014)</td>
										<td>当該小班が所在する市町村の名称</td>
										<td>文字列型（CharacterString）</td>
									</tr>
									<tr>
										<td>樹種１<br>(A45_015)</td>
										<td>当該小班に生育する樹種のうち、森林計画の樹立年度時点での面積歩合が一番大きい樹種</td>
										<td>コードリスト「<a href="/ksj/gml/codelist/jushuCd.html" target="_blank">樹種コード</a>」</td>
									</tr>
									<tr>
										<td>樹立林齢１<br>(A45_016)</td>
										<td>樹種1の森林計画樹立年度時点での林齢</td>
										<td>整数型（Integer）</td>
									</tr>
									<tr>
										<td>最新林齢１<br>(A45_017)</td>
										<td>樹種林齢1に、森林計画樹立後の経過年数を加算した林齢</td>
										<td>整数型（Integer）</td>
									</tr>
									<tr>
										<td>樹種２<br>(A45_018)</td>
										<td>当該小班に生育する樹種のうち、森林計画の樹立年度時点での面積歩合が二番目に大きい樹種</td>
										<td>コードリスト「<a href="/ksj/gml/codelist/jushuCd.html" target="_blank">樹種コード</a>」</td>
									</tr>
									<tr>
										<td>樹立林齢２<br>(A45_019)</td>
										<td>樹種2の森林計画樹立年度時点での林齢</td>
										<td>整数型（Integer）</td>
									</tr>
									<tr>
										<td>最新林齢２<br>(A45_020)</td>
										<td>樹立樹種2に、森林計画樹立後の経過年数を加算した林齢</td>
										<td>整数型（Integer）</td>
									</tr>
									<tr>
										<td>樹種３<br>(A45_021)</td>
										<td>当該小班に生育する樹種のうち、森林計画の樹立年度時点での面積歩合が三番目に大きい樹種</td>
										<td>コードリスト「<a href="/ksj/gml/codelist/jushuCd.html" target="_blank">樹種コード</a>」</td>
									</tr>
									<tr>
										<td>樹立林齢３<br>(A45_022)</td>
										<td>樹種3の森林計画樹立年度時点での林齢</td>
										<td>整数型（Integer）</td>
									</tr>
									<tr>
										<td>最新林齢３<br>(A45_023)</td>
										<td>樹立林齢3に、森林計画樹立後の経過年数を加算した林齢</td>
										<td>整数型（Integer）</td>
									</tr>
									<tr>
										<td>計画区名称<br>(A45_024)</td>
										<td>当該小班が所在する森林計画区の名称</td>
										<td>文字列型（CharacterString）</td>
									</tr>
									<tr>
										<td>林種の細分<br>(A45_025)</td>
										<td>森林を成立状態により区分したもの</td>
										<td>コードリスト「<a href="/ksj/gml/codelist/rinshunosaibunCd.html" target="_blank">林種の細分コード</a>」</td>
									</tr>
									<tr>
										<td>機能類型<br>(A45_026)</td>
										<td>重視すべき機能</td>
										<td>コードリスト「<a href="/ksj/gml/codelist/kinouruikeiCd.html" target="_blank">機能類型コード</a>」</td>
									</tr>
									<tr>
										<td>面積<br>(A45_027)</td>
										<td>当該小班の面積。単位はhaとする</td>
										<td>実数型（Real）</td>
									</tr>
									<tr>
										<td>保安林１<br>(A45_028)</td>
										<td>保安林に指定されているか否か、また、指定されている場合にはその内容（最大4つまで）</td>
										<td>コードリスト「<a href="/ksj/gml/codelist/hoanrinCd.html" target="_blank">保安林コード</a>」</td>
									</tr>
									<tr>
										<td>保安林２<br>(A45_029)</td>
										<td>保安林に指定されているか否か、また、指定されている場合にはその内容</td>
										<td>コードリスト「<a href="/ksj/gml/codelist/hoanrinCd.html" target="_blank">保安林コード</a>」</td>
									</tr>
									<tr>
										<td>保安林３<br>(A45_030)</td>
										<td>保安林に指定されているか否か、また、指定されている場合にはその内容</td>
										<td>コードリスト「<a href="/ksj/gml/codelist/hoanrinCd.html" target="_blank">保安林コード</a>」</td>
									</tr>
									<tr>
										<td>保安林４<br>(A45_031)</td>
										<td>保安林に指定されているか否か、また、指定されている場合にはその内容</td>
										<td>コードリスト「<a href="/ksj/gml/codelist/hoanrinCd.html" target="_blank">保安林コード</a>」</td>
									</tr>
									<tr>
										<td>保護林<br>(A45_032)</td>
										<td>保護林に設定されているか否かの区分</td>
										<td>コードリスト「<a href="/ksj/gml/codelist/hogorinCd.html" target="_blank">保護林コード</a>」</td>
									</tr>
									<tr>
										<td>緑の回廊<br>(A45_033)</td>
										<td>緑の回廊に指定されている場合、その名称を示すコード</td>
										<td>コードリスト「<a href="/ksj/gml/codelist/midorinokairoCd.html" target="_blank">緑の回廊コード</a>」</td>
									</tr>

"""

# Parse the HTML content
# HTMLコンテンツを解析
soup = BeautifulSoup(html_content, "html.parser")

# データを抽出
data = {}
rows = soup.select("tr")

# 各行を反復処理
for row in rows:
    cells = row.find_all("td")
    if len(cells) > 0:
        # キーを括弧内のテキストから抽出
        key = cells[0].get_text(strip=True).split("（")[-1].rstrip("）")
        # 値を括弧前のテキストから抽出
        value = cells[0].get_text(strip=True).split("（")[0]
        data[key] = value

# 結果をJSON形式に変換
json_output = json.dumps(data, ensure_ascii=False, indent=4)

# JSONファイルに保存
with open("_properties.json", "w", encoding="utf-8") as f:
    f.write(json_output)

print("JSONファイルが作成されました。")
