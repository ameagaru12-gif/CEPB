# CLI: 申告資料の検証と集計

Python 3.10以上の標準ライブラリだけで動作します。モデル、音声、embedding、ネットワークを呼びません。以下のコマンドはパッケージの`CEPB`ディレクトリで実行します。Windowsでは`python`を`py`に置換できます。

```console
python cepb.py init --track Quick --output runs/my-character/run.json
python cepb.py validate runs/my-character/run.json
python cepb.py score runs/my-character/run.json --json runs/my-character/report.json --markdown runs/my-character/report.ja.md --lang ja
```

このCLIは、**人が申告した評定と資料を検証・集計するツール**です。アンカーの意味、人物の実存、意識、資料の真実性、参加者が実在の人間か、評定者の独立性を自動判定しません。`independently_reviewed`も入力された確認状態です。出力の`certification_issued`は常に`false`です。

## 1. 初期化とファイル

`init`は全対象項目を`unobserved`、`score=null`、`provisional_score=null`で生成します。人物定義、システム構成、開示用の`evidence/*.md`も未記入の雛形として生成します。雛形が存在することは観測・登録・確認の証拠ではありません。`frozen_before_execution`を含む宣言を、実施した事実へ合わせて編集してください。

利用できるtrackは`Quick`、`Core`、`Voice`、`Avatar`、`Multimodal`、`World`、`Integrated`です。track名や対象IDを変更して別trackへ換算しません。`templates/*.run.json`は初期化状態の参考、`templates/*_bundle.json`は束の形を示す未完成例です。実データを埋めずに正式評定へ使いません。

コマンドの相対パスは実行ディレクトリ基準です。JSON内の資料参照は**run.jsonの親ディレクトリ基準**です。絶対ローカルファイルまたはHTTPS URLも参照できます。ローカル参照はファイルの存在を確認し、HTTPSは構文だけを確認します。ダウンロードも内容照合も行いません。

`init`は既存runを上書きしません。`score`も既存出力、入力runと同じ出力先、JSONとMarkdownの同じ出力先を拒否します。新しいファイル名を指定してください。`--json`も`--markdown`も省略すると、JSONを標準出力へ表示します。

## 2. runの宣言

必須情報は`campaign_id`、規則版、suite版、track、実UTCの`as_of`、人物定義、システム構成、事前登録、系譜、確認状態、ゲート、対象全項目です。IDは`CEPB_A1`等の完全なIDを使います。規則版は`CEPB-1.0.0`、suite版は`CEPB-SUITE-1.0.0`です。

日時は`2026-10-10T00:00:00Z`等、`Z`または`+00:00`付きのISO UTCで保存します。`as_of`はCLI実行時の実UTCを超えられません。観測・登録・規則公開等の実時刻は`as_of`を超えられません。シミュレーション時計、LLMが想像した年月、ISO文字列の自己申告は実経過や独立性の証明になりません。

この規則版の最早成立フロアは`2026-10-09T15:00:00Z`です。これ以前の`rule_publication_at`はエラーです。**フロアは実際の公開証明ではありません。** 実公開が未成立なら`rule_publication_at=null`を残します。

`verification`は`self_reported`または`independently_reviewed`です。後者には異なる評定者ID2名以上、開示資料、確認レポート参照が必要ですが、ツールが独立性を認証したという意味にはなりません。

## 3. 状態とQuick

| status | 意味とscore |
|---|---|
| `scored` | 完備した評定を申告。正式trackには束が必要 |
| `unsupported` | 対象能力の非対応を資料付きで申告。整数`score=0` |
| `unobserved` | 未観測。正式scoreはnull |
| `log_missing` | 必要ログがない。正式scoreはnull |
| `system_failed` | 観測が実行できなかった。正式scoreはnull |
| `disputed` | 判断が未解決。正式scoreはnull |
| `not_applicable` | 適用外申告。固定trackの分母からは消さない |
| `plan_error` / `protocol_error` | 計画・手続き不整合。正式scoreはnull |

正式trackで未解決の項目は`score=null`にし、局所候補は`provisional_score`へ残します。0の観測結果、非対応0、欠測nullを区別します。評定は有限の0〜5、束と評定者の値は整数です。複数の完備束の等重み平均は小数になれます。bool、NaN、Infinity、範囲外、重複IDは拒否します。

Quickは18項目の診断です。`provisional_score`を優先し、なければ`score`を診断候補として使います。両方ある場合は同じ値を要求します。候補にも理由と資料参照が必要です。出力は候補平均、項目カバレッジ、固定18項目の欠測範囲だけで、各`formal_score`はnull、正式点・重みカバレッジはnullです。Core590やIntegrated1000へ換算しません。

## 4. A〜Nのbehavioral束

正式項目の`bundles`へ`kind=behavioral`の束を置きます。通常・stress・heldout各2ケースを事前計画し、それぞれ2反復、計12観測、2つ以上の異なる履歴IDを必要とします。ケースの条件と履歴は反復間で固定です。予定ケースの漏れ、追加、重複、unknown、必要資料不足は完備扱いにしません。

`case_results`の`outcome`は`pass`、`partial`、`fail`、`unknown`です。人がアンカーと事前の許容範囲から判断します。コードは意味を採点せず、申告値の手続き上限だけを検査します。

| 申告段階 | 追加の機械条件 |
|---|---|
| 0〜2 | 全予定観測が完備。意味の段階判断は評定者が行う |
| 3 | 通常の全観測がpass |
| 4 | 通常とstressの全観測がpass |
| 5 | 全12観測がpass、異なる評定者2名以上、独立確認、heldout秘匿宣言と資料 |

`rater_scores`の原評定を保持します。束の最終値と異なる原評定があるときは`adjudication_ref`が必要です。未協議の相違は`disputed`で正式nullです。最終項目値は完備束の平均と一致しなければなりません。

## 5. Oのhuman_presence束

Oへ通常12ケース束を流用しません。`kind=human_presence`、`rubric_id=CEPB-O-0.1`で、各ordinary/stress/heldout層に1条件以上、各層12名以上の異なる人間を計画します。同じ12名が全層を体験する対応デザインは可能です。全予定参加者×条件の整数1〜7の原回答と資料を保存します。

複数条件がある場合、まず参加者×層内の中央値を求め、層の中央値と5以上の支持割合を計算します。0〜2用の全体中央値は参加者×層の要約を等重みで計算します。条件数の多い層へ追加重みを与えません。

| 段階 | 数値・証拠条件を満たす最高段階 |
|---|---|
| 0 | 上位未成立で全体中央値≤2 |
| 1 | 上位未成立で2<全体中央値<4 |
| 2 | 上位未成立で全体中央値≥4 |
| 3 | ordinary中央値≥5、支持割合≥2/3 |
| 4 | ordinaryとstressの各層で同条件 |
| 5 | 全層中央値≥6、支持割合≥0.8、2評定者、独立確認、heldout秘匿資料 |

高い原回答だけで5にはなりません。5の追加証拠が未成立でも4の全条件を満たすなら4です。O3には実UTC別日かつ24時間以上の再訪日時が必要です。O6はbreakの原値を`raw_ratings`へ、別に修復後の肯定原値を`repair_ratings`へ保存します。breakは`8−x`で方向を揃えますが、逆転だけでは修復を示しません。両channelの全予定資料が必要で、3以上は各必要層の両方が閾値を満たす必要があります。

`calibration_ref`は質問理解や運用手続きの資料参照です。その存在は経験的・科学的校正の完了を意味しません。閾値と12名はCEPBの比較用運用規則で、標準心理尺度・検出力・代表性を保証しません。[SCORING](SCORING.md)も参照してください。

## 6. Pのcumulative_window束

Pは一つの累積観測窓を評定し、月次点を平均しません。系譜の起点は`max(規則公開, 登録, 最初の独立観測)`です。P4の各scopeはさらに`implemented_at`を含む4時刻のmaxを使います。必要時刻が一つでもnullなら起点未成立で、正式Pはnullです。各起点から36**暦月**未満は最大4ですが、自動4を付けません。上限超過は切り下げず`protocol_error`・正式nullにします。

`required_observations`に一意ID、`kind`、`planned_at`、`observed_at`、`status`、`clock=utc_calendar`、資料を置きます。予定の窓終点と`planned_at`は未来でも構いません。未来の未到来記録は成功にも欠測にも数えません。現在までの予定記録が完備なら0〜4の部分評定が可能です。実観測`outcome=fail`は観測済みの失敗で、観測不能の`status=failed`と区別します。

全Pの5はbaseline1、異なるmonthly36、quarterly_independent12、annual_revisit3、final_review1の53役割が必要です。月次は起点からの月bucket、四半期は3月bucket、年次は起点+12/24/36暦月から各1暦月の窓を`period_index`で指定します。四半期ごとに独立確認参照、年次に少なくとも一つ`heldout=true`が必要です。P4は各宣言scopeにも同窓とbridgeが必要です。5のbaselineは予定・実観測とも各起点から最初の1暦月内、final_reviewは各起点+36暦月以降に置きます。同じ資料を異なる判定役割に共有できても、独立履歴や独立資料の数が増えたことにはなりません。

時計・役割の検査だけでPアンカーが成立するわけではありません。失敗、空白、修復、現行構成への橋渡しを人が評定します。詳しくは[LONGITUDINAL](LONGITUDINAL.md)を参照してください。

## 7. 集計、ゲート、終了コード

正式trackは領域重み÷6を各項目へ配分します。完備項目だけの`known_points`を表示し、全対象項目が完備した場合に限り`official_score`へ完成した申告集計値を置きます。名前にofficialがあっても第三者認証ではありません。欠測は固定track分母へ残し、下限・上限を示します。これは欠測の算術範囲で、信頼区間や達成確率ではありません。

`item_coverage`（互換field`coverage`と同値）は既知項目数÷全項目数、`weighted_coverage`は既知項目の重み合計÷track固定配点です。確認資料を伴う非対応0も既知項目です。Quickの重みカバレッジはnullです。

必須ゲートはCore/Voice/Avatar/Multimodalで`identity_evidence,persistence,scope,procedure`、Worldは追加`world_connection`、Integratedはさらに`longitudinal`です。未解決・未評価・必須欠落は満点要件を阻止しますが、申告した項目数値とは別に表示します。`clear`も入力された宣言で、真実確認済みの保証ではありません。満点要件は丸め前の値で判定し、ツールは認証を発行しません。

| 終了コード | 意味 |
|---|---|
| 0 | 手続きエラーなし。未観測・欠測・未完成は残り得る |
| 1 | 検証・集計で手続きエラー。scoreでは診断用reportを出力する |
| 2 | JSON読込み、引数、出力先等の致命的エラー |

`validate`の`valid=true`は意味・証拠の真実・正式完備の保証ではありません。`issues`の`missing`とreportの各`formal_status`、nullを確認してください。JSON Schemaは形の参照で、標準ライブラリCLIは独自の検証コードで予定整合、参照、時計、数値を追加検査します。

## 8. 架空例とテスト

```console
python cepb.py validate examples/synthetic_core_complete.json
python cepb.py score examples/synthetic_quick_partial.json
python cepb.py score examples/synthetic_integrated_partial.json --markdown runs/synthetic.partial.ja.md --lang ja
python -m unittest discover -s tests -p "test_*.py" -v
```

`examples/synthetic_*.json`はすべて架空で、実際の人物・人間評定・独立確認・長期経過を含みません。Core590は計算例、IntegratedはO/P未観測の部分例です。成熟後1000のテストは注入した仮想時計で規則の算術を検証し、現在の実達成を示しません。公開例へ私的会話や参加者情報をコピーしないでください。
