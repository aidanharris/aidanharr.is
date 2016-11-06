Glossary
########
:date: 2016-06-09 15:40
:author: aidanharris
:slug: glossary
:status: published
:url: glossary/
:save_as: glossary/index.html
:template: page

This page contains descriptions of any technical terms used on this
website:

[child-pages depth="1" class="mdl-list"]

::


    $('.mdl-list .page_item').each(function(){var href = $(this).find('a:first').attr('href'); console.log(href);$(this).replaceWith(
    '<li class="mdl-list__item"><span class="mdl-list__item-primary-content">' + $(this).find('a:first').get()[0].outerHTML + '</span></li>');});

