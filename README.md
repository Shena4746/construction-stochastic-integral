# TeX Template in VSCode

## What's This?

VSCode で TeX を書くとき備忘録兼テンプレ.

- `/.vscode`: latex-workshop 拡張機能の設定等
- `/.tex`: docmute 等を使ってファイル分割して書く用のテンプレート
- `/.pdf`: `/.tex` の中身をビルドしたサンプル
- `/.cspell`: Code Spell Checker 拡張機能用のホワイトリスト
- `.chktexrc`: TeX 用 Linter chktex のオプション指定

## .vscode

### settings.json

主に, Latex-workshop 拡張機能の使用を前提とした Build 周りの設定が書いてある.
`latex-workshop.latex.tools` で定義された `command` を `latex-workshop.latex.recipes` から, 任意に命名された名前によって呼ぶことで Build される.
レシピは `latexmk` を用いた以下の名前の2つを定義してある:

- latexmk-English: ほぼ?英文専用の `pdflatex` によるシンプルな高速版
- latexmk-LuaLaTeX: フォント管理や日本語対応など多機能な `LuaLaTeX` による低速版

以下のように, 後者をデフォルトとしている. 執筆時は前者を使って, 仕上げに後者を使うなどの分担もアリかもしれない.

```
"latex-workshop.latex.recipe.default": "latexmk-LuaLaTeX",
```

### tasks.json

ビルド過程で生成される中間ファイルを手動で全削除するもの. [fd コマンド](https://manpages.ubuntu.com/manpages/bionic/ja/man1/fd.1.html) に依存.

## TeX Template

素朴な方法で1つの tex ドキュメントを1つの tex ファイルに詰め込んで書くと, ビルドにかかる時間やコンパイルエラー時の問題の切り分け, 部分的なレビューのやり辛さなど様々な面で非効率な状況が生じてしまう. docmute パッケージは, この問題を緩和する手段の1つとして, 複数に分割された tex ファイルを1つの tex ファイルにまとめてビルドする機能を提供する.

master.tex を見ればファイル分割と inclusion の方法は分かるはず.
master.tex にあるように, 親ファイルにて `\usepackage{docmute}` とした上で, `\input(your-tex-file-to-be-included)` によって子ファイルを読み込むとき, 子ファイルのプリアンブルは無視され, 親ファイルのプリアンブルが親子結合後のドキュメント全体に適用される.
したがって, 子ファイル執筆時は子ファイル専用のプリアンブルを子ファイルに書いてよい. 子ファイル完成後に子ファイルを親ファイルと結合させるための手間は, 親ファイル側でのみ発生して, 子ファイル側では発生しない.

## .chktexrc

chktex ( TeX 用の Linter 的なもの ) 実行時に与えるオプションを設定できる. たとえば, 12番と13番のエラーを表示しないようにするには以下のように書く.

```
CmdLine
{
    -n12 -n13
}
```

## Snippets

<https://github.com/Shena4746/LaTeX-Snippets-for-VSCode> を参照.
