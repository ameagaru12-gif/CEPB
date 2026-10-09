# CEPB — AIキャラクター実存度ベンチマーク

**日本語** | [English](README.md)

CEPBは、AIキャラクターが識別できる人物・履歴を維持し、現在の状況へ応答し、固有の見方を表し、言葉と観測できる結果を接続する程度を評価します。機能としての連続性、媒体と世界の能力、利用者が感じる存在感、長期の証拠を分けて報告します。

**バージョン1.0.0・16領域96項目・MITライセンス・Python標準ライブラリのみ。** 実施可能な評価手順とツールを揃えた版です。配点・閾値・最低件数は運用規則であり、意識や人格の存在を科学的に測定する校正済み尺度ではありません。このリポジトリで認証機関や公開ランキングを運営しているわけではありません。

## 用途を選ぶ

| 区分 | 用途 | 結果 | 入口 |
|---|---|---|---|
| **CEPB Quick** | 小さな予算で開発上の改善点を見つける | 代表18項目の局所候補0〜5とカバレッジ。Core完成点にはしない | [Quickガイド](tracks/quick/README.ja.md) |
| **CEPB Core** | 文字型も含むAIキャラクターの基本性能を比較する | 54項目、固定上限 **590点** | [Coreガイド](tracks/core/README.ja.md) |
| **CEPB Integrated** | 宣言したシステム全体を評価する | 96項目、固定上限 **1000点**。姿・声・世界への作用・人の存在感・長期実証を含む | [Integratedガイド](tracks/integrated/README.ja.md) |
| **CEPB Verified** | Quick・Core・Integratedの結果を第三者が検証する | 検証範囲、独立評定、再現した観測、責任主体を示す報告 | [Verifiedガイド](tracks/verified/README.ja.md) |

Verifiedは検証の区分であり、第四の配点体系ではありません。自己申告のフラグやCLIの実行だけでは第三者検証済みになりません。第三者が確認したQuickも診断版のままです。

個別用途向けに、**Voice 660点・Avatar 660点・Multimodal 790点・World 720点**も用意しています。同じクラス、人物モード、試験版、言語、運用条件で比較します。[用途別の選び方](docs/ja/USE_CASES.md)。

## 手元で試す

Python 3.10以上を使います。保存済み評定の集計にAPIキー、モデルサービス、パッケージのインストール、ネット接続は不要です。この `CEPB` フォルダを作業場所にしてください。Windowsでは `python3` を `py` に置き換えられます。

```sh
python3 cepb.py init --track Quick --output my_quick.json
python3 cepb.py validate my_quick.json
python3 cepb.py score my_quick.json --json my_quick_report.json --markdown my_quick_report.md --lang ja
```

新しい計画の証拠は未観測から始まります。空テンプレートは試験済みのシステムではありません。[ケースカード](docs/ja/CASEBOOK.md)を実施し、実入力と利用者へ届いた出力を保存して、評定と根拠参照を記入した後に集計します。`score` は提出された評定の検査と集計を行います。対話の生成や意味品質の自動採点は行いません。

正式なCore・Integratedでは実施前に計画を固定し、項目の試験束を完成させます。標準の挙動試験束は、通常2ケース・難条件2ケース・独立に準備した未使用2ケースを各2回反復し、少なくとも2履歴へ割り付けます。公開カードは開発例と生成手順です。公開された例を秘密の未使用試験として使えません。

```sh
python3 cepb.py init --track Core --output my_core.json
python3 -m unittest discover -s tests -v
```

[CLIと記録形式](docs/ja/CLI.md)、[アダプターガイド](docs/ja/ADAPTER_GUIDE.md)も参照できます。証拠が未完備なら分母を固定したままカバレッジと欠測算術範囲を示し、完成点を作りません。

## 仕様を読む

1. [共通仕様](docs/ja/SPECIFICATION.md)：定義、クラス、人物モード、実装プロフィール、採点範囲。
2. [96項目のアンカー](docs/ja/ITEMS.md)と[ケース集](docs/ja/CASEBOOK.md)：観測対象と反証。
3. [採点手順](docs/ja/SCORING.md)：試験束、欠測、体験の原評定、集計。
4. [長期観測](docs/ja/LONGITUDINAL.md)：前向き登録、実暦、保守、新範囲。
5. [第三者検証](docs/ja/VERIFIED.md)、[研究上の位置づけと妥当性](docs/ja/RESEARCH_AND_VALIDATION.md)。

Pの6項目の5には、**前向きに登録した36暦月の実証**が必要です。成熟前の上限は4ですが、証拠がなければnullであり、自動的に4点にはなりません。新しく認定する範囲には別の時計を設けます。これは証拠の規則であり、技術進歩の時期の予測ではありません。過去ログ、仮想時計、並列cloneで期間を代用できません。

## フォルダの構成

```text
CEPB/
  README.md / README.ja.md       日英の入口
  tracks/                       Quick / Core / Integrated / Verified
  docs/en/ / docs/ja/            同等の文書
  data/items.json                日英の正本項目と固定配点
  data/cases.json                日英の公開ケースカード
  cepb.py                        オフライン検査・集計CLI
  schemas/ / templates/          記録形式
  examples/                      架空と明示した記入例
  tools/                         可搬性と公開前の検査
  tests/                         計算・手続きの回帰試験
  LICENSE / NOTICE / CITATION.cff
```

文書リンクは相対参照で、このフォルダだけを独立リポジトリへコピーできます。キャラクターエンジン、私的対話、個人の評定、権利のあるアバター、第三者の論文は同梱していません。評価者は自分の資料に適用される権限に従って根拠を保管します。[パッケージ検査記録](PACKAGE_CHECKS.md)に、回帰試験と単独動作の結果、再現用コマンドを記載しています。

## 参加と再利用

独自のコード・文書・合成ケースは[MITライセンス](LICENSE)で利用・改変・再配布できます。リンク先の研究は各資料の権利に従います。[貢献ガイド](docs/ja/CONTRIBUTING.md)、[運営と版管理](docs/ja/GOVERNANCE.md)、[変更履歴](CHANGELOG.md)、[引用情報](CITATION.cff)に、今後の変更と比較を保つ手順を記載しました。

複数領域と評価範囲の明示は[HELM](https://arxiv.org/abs/2211.09110)、課題群の更新は[Dynabench](https://aclanthology.org/2021.naacl-main.324/)の方向性を参考にしています。これらの研究がCEPB固有の項目や閾値を実証したとは扱いません。
