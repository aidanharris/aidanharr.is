Title: Switching from 1Password to Pass
Id: 8
Date: 2017-05-27 18:21
Author: aidanharris
Slug: switching-from-1password-to-pass
Status: published
HeadingTheme: light
HeadingIconFont: fa fa-key
BeforeHeading: &nbsp;

I've decided to switch password managers from [1Password](https://1password.com/) to [Pass](https://www.passwordstore.org/). This blog post will detail my thoughts on the subject and explain the pros and cons of doing so.

Before I get started I feel like I wouldn't be doing my civic duty if I didn't take this time to tell you to use a password manager if you're not doing so already:

# **\*USE A PASSWORD MANAGER**


### Why Pass?

You might be wondering why I'd choose pass, heck you might not have even heard of it before reading this ("pass" isn't exactly a very SEO friendly name). "What's wrong with 1Password" you might ask. Well as it turns out, a lot of things. Don't get me wrong it's a very good password manager and if it works for you then great. However I feel like I've gotten to the point where 1Password no longer suits my needs. 1Password was great while I was operating in the Apple bubble. Once upon a time I had an iPhone, an iPad and a Macbook and all was well with the world. Then I discovered the big bad <strike>Linux</strike> GNU/Linux 🐧 (that's a penguin, for the uninitiated - or those without a decent font that supports <strike>emoji</strike> Unicode).

Believe it or not 1Password works surprisingly well under GNU/Linux using [Wine](https://www.winehq.org). The main issues I have with 1Password are as follows:

#### Closed source

While I have no reason to doubt that 1Password is in any way, shape, or form compromised, I can't help but feel that the strong and stable (pun intended) foundations of git and gpg hugely benefit pass over the black-box of 1Password.

#### Synchronisation

Local file synchronisation is a massive pain with 1Password. I refuse to use Dropbox and iCloud sync doesn't work on Windows or GNU/Linux so that's out of the question too. My current solution to this conundrum is a hodgepodge of [Syncthing](https://syncthing.net) and using the wifi-sync. This is **not** scalable and could no doubt cause problems if I continue down this path. Using git completely side-steps this issue altogether. I can sync using a local git repository or a private remote repository.

### Disadvantages of Pass

While I see Pass as the way forward, it's not all bright and rosy, there are some things that I dislike about it.

* Hard to migrate - [pass-import](https://github.com/roddhjav/pass-import) exists but it didn't want to work at all. I'm now in a laborious process to slowly migrate each and every password I've built up over the years from 1Password to Pass. Not Good!
* Mobile Integration? - It looks like there's solid Android integration, iOS may be a challenge ;)
* Winblows - [Pass4Win](https://github.com/mbos/Pass4Win) exists but is deprecated, WSL despite its hype doesn't support USB devices and I don't trust Windows enough to leave my GPG keys lying around. I guess I could use Virtualbox with USB pass-through for my Yubikey. I don't do any serious work on Windows anyway though, so I doubt this will be an issue.
* No support for storing files - I can botch it by base64 encoding files and may be able to simply store the files in the git repo but not sure how that'll work on other devices.

### Conclusion

Despite its shortcomings I feel that pass is the way to go. It's more scalable than 1Password and is built on top of a rock solid foundation of gpg and git. It also doesn't hurt that it has solid integration with [dmenu](https://github.com/klaasb/passdmenu) :).

<small>*Big bold text added, for dramatic effect</small>
