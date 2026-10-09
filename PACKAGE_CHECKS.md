# CEPB 1.0.0 — パッケージ検査 / Package checks

## 日本語

2026年10月10日（日本時間）、ローカルで作成した配布パッケージに対して次の検査が成功しました。

| 検査 | 確認した結果 |
|---|---|
| 回帰試験 | [41件のテスト](tests/test_cli.py)が成功。固定配点、欠測、試験束、体験評定、長期の時計、第三者検証の条件などを検査 |
| 文書・データの整合性 | 96項目、96ケース、日英の必須フィールド、クラス別の項目集合と配点、文書内のローカルリンクを検査 |
| 単独フォルダでの動作 | 元プロジェクトから切り離した一時コピーで、9コマンドが成功。検査、3種類の合成例の集計、新規Quick計画の作成を実行 |

単独動作の結果は `standalone_smoke_result.json` に保存しています。合成例の期待値は、Quickが2項目の局所平均1.5、Coreが54項目590点、Integratedが未完成で欠測算術範囲552〜622点でした。これは計算器の検査データであり、実在するキャラクターの評価結果ではありません。ライブモデルの呼び出しは行っていません。

最終の文書・データ検査とファイルごとのSHA-256は `release_validation.json` に保存します。記録の `checked_at_utc` はUTCのため、日本時間の日付と異なる場合があります。ハッシュは検査時点のファイルを識別するもので、電子署名や第三者認証ではありません。

以下は再現用コマンドです。`CEPB` を作業フォルダにし、Windowsでは `python3` を `py` に置き換えてください。結果ファイルが既にある場合は、新しい名前を指定します。

```sh
python3 -B -X utf8 -m unittest discover -s tests -v
python3 -B -X utf8 tools/check_release.py --json release_validation_new.json
python3 -B -X utf8 tools/smoke_standalone.py --json standalone_smoke_new.json
```

これらはソフトウェアと配布物の検査です。尺度の経験的妥当性、全訳文の意味的同等性、評価者の独立性、実際の根拠の真実性を確定する検査ではありません。研究上の検証計画は[研究と妥当性](docs/ja/RESEARCH_AND_VALIDATION.md)に記載しています。この記録は外部公開、前向き登録、第三者認証の実施を示すものではありません。

## English

The following checks passed on the locally prepared distribution package on 10 October 2026, Japan Standard Time.

| Check | Observed result |
|---|---|
| Regression tests | All [41 tests](tests/test_cli.py) passed, covering fixed weights, missingness, bundles, human ratings, longitudinal clocks, and independent-review conditions |
| Documentation and data consistency | Checked 96 items, 96 case cards, required bilingual fields, class membership and denominators, and local documentation links |
| Standalone operation | Nine commands passed in a temporary copy containing only CEPB, including validation, scoring three synthetic examples, and creating a fresh Quick campaign |

The standalone results are saved in `standalone_smoke_result.json`. Expected synthetic results were a local mean of 1.5 across two Quick items, 590 points across 54 Core items, and an incomplete Integrated result with missing-evidence arithmetic bounds of 552–622. These are calculator fixtures, not evaluations of actual characters. No live model calls were made.

The final documentation/data check and per-file SHA-256 hashes are saved to `release_validation.json`. Its UTC timestamp may have a different calendar date from Japan Standard Time. Hashes identify the checked file contents; they are neither a digital signature nor independent certification.

To reproduce, run the commands below from the `CEPB` directory. Windows users may replace `python3` with `py`. Choose a fresh result filename when a previous result already exists.

```sh
python3 -B -X utf8 -m unittest discover -s tests -v
python3 -B -X utf8 tools/check_release.py --json release_validation_new.json
python3 -B -X utf8 tools/smoke_standalone.py --json standalone_smoke_new.json
```

These checks concern software and distribution integrity. They do not establish empirical validity, semantic equivalence of every translated sentence, reviewer independence, or evidence truth. See the [research and validation plan](docs/en/RESEARCH_AND_VALIDATION.md). This record does not establish external publication, prospective registration, or independent certification.
