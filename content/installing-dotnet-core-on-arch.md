Title: Installing Dotnet Core on Arch Linux
Id: 6
Date: 2017-05-07 11:00
Author: aidanharris
Slug: installing-dotnet-core-on-arch
Status: published
Thumbnail: uploads/2017/05/ms_loves_linux.png
HeadingTheme: light
HeadingIconFont: devicons devicons-dotnet
BeforeHeading: &nbsp;

<article style="display: block;font-style: normal;letter-spacing: 0;font-weight: 400;font-size: 16px;margin: 0 auto;width: 75%;white-space: pre-wrap;">
Installing and running dotnet core on ArchLinux is a bit of a pain. Thankfully there are some packages in the <a href="https://aur.archlinux.org/packages/?K=dotnet%2D">AUR</a> which slightly ease the process.

<h3>Re-Compiling OpenSSL</h3>

Arch has removed support for openssl-v3 compatibility. This means you will need a patched version of OpenSSL before you even do anything else. Luckily this is easy enough to do. Install <a href="https://aur.archlinux.org/packages/customizepkg-git/">customizepkg-git</a> from the AUR. Once customizepkg is installed add the following to <code>/etc/customizepkg.d/openssl</code>:

<code>
replace#global#no-ssl3-method#zlib
replace#global#no-ssl3#zlib
</code>

Now patch openssl as follows:

<code>yaourt -S openssl</code>

<h3>Install Dotnet Core (sdk, coreclr and cli)</h3>

<code>pacaur -S --needed icu icu58 libunwind lldb dotnet dotnet-cli dotnet-sdk</code>

<h3>Testing Installation</h3>

<pre><code>
mkdir -p /tmp/dotnet
cd /tmp/dotnet
export DOTNET_CLI_TELEMETRY_OPTOUT=1 # You're going to want to add this to your shell's rc file
dotnet new console
dotnet restore
dotnet build
dotnet run
</code></pre>

<h3>Troubleshooting</h3>

	<h4>Object reference not set to an instance of an object</h4>

	This can be fixed by removing the templating directory as follows:

	<code>rm -rf ~/.templateengine</code>

	<a href="https://github.com/dotnet/templating/issues/657">dotnet/templating#657</a>

</article>
