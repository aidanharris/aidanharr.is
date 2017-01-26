# [aidanharr.is](https://aidanharr.is)

This repository contains the source code and articles for the personal website of Aidan Harris (me).

You can find licensing information in [LICENSE](https://github.com/aidanharris/aidanharr.is/blob/master/LICENSE), note that this license does not take precedence over any other third-party code or content.

As for how the website is built, it uses the excellent [Pelican](https://github.com/getpelican/pelican/) which I highly recommend you check out.

## Articles

Articles are housed in the [content](https://github.com/aidanharris/aidanharr.is/tree/master/content) sub-directory. Should you find any mistakes or want to enhance the content in any way, pull-requests are welcome.

## Building

### CSS

```bash
git clone https://github.com/aidanharris/aidanharr.is
cd aidanharr.is
cd theme/simple/templates
npm i
gulp
```

### HTML

HTML can be built using the provided Makefile as follows:

```bash
make html
```

Note, that the HTML is minified using html-minifier so you will need to install this globally using `npm install -g html-minfier`
