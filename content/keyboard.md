Title: My Keyboard Configuration  
Author: Fábio Fortkamp
Date: 2015-09-17  
Category: Article  
Tags: keyboard, setup
Slug: keyboard  
Status: published  

I'm a little picky about how I use a keyboard to type things into a computer, so here is my current setup.

## Hardware I use

On the hardware side, when it's possible, I use the [Microsoft Wireless Desktop 800](http://www.microsoft.com/hardware/en-us/p/wireless-desktop-800/2LF-00001Microsoft Wireless Desktop 800 ) 
 series. They are not the cheapest options in the market, but they are neither the most expensive. I find them very confortable to type, the manufacturer is reliable, and I've been overall very pleased. When my MacBook Pro is not mounted on a desk, its built-in keyboard is also very good.

## Software to modify the keyboard's behaviour (OS X)

I mentioned "hardware side" because, for me, it would be impossible to use a keyboard without some software to modify it. It all started when I learned to use [Emacs](https://www.gnu.org/software/emacs/ ) 
 and Linux, back in 2010. Emacs is a text editor that makes a *heavy* use of the `Ctrl` key, located on the bottom-left corner of any modern keyboard. As soon as you start reading about Emacs and trying to master it, the number one tip is *remap your Caps Lock key to a Control key*, to take advantage of its excellent position (right on the keyboard's home row).

The Caps Lock key, to me, is completely useless. I'm not 15 anymore and so I don't have to yell at people on the Internet or post gramatically-incorrect comments on Facebook. In the very rare situation I have to type a word in upper case, I just keep the Shift button pressed -- I type so few letters in upper case that this barely slows me down. Besides, there are a lot of scripts and hacks to press a keyboard shortcut and automatically convert a word or a sentence to upper case; Emacs has its commands and the *Edit* menu in many OS X applications has a function to do that.

So, the Caps Lock on my computer behave like a Control key. Try it yourself: even if you use Windows and Word, see if typing `<Caps Lock>-C` is not easier than typing `Ctrl-C`. You're welcome.

But there is more! Like I said, now I have a Control key (which, may we remember, is very important to use with Emacs but is also prominent in standard text shortcuts is OS X) in the keyboard home row, in the left side. How nice would it be to have a Control key on the right side, making it much easier to, for instance, typing `Ctrl-A`? The natural candidate for this is the `Return`(or `Enter`) key, but this key is not useless. However, when you want to press return, you *just press return and they release the key*. Keeping the `Return` key pressed, so that you can also type a second key, should not disturb your typing (keeping the `Enter` key pressed to insert a bunch of newlines is not something I do). So the `Return` key, when pressed alone, is a `Return` key; when pressed with other letters, is a `Ctrl` key.

I, as an engineer, cannot accept the asymmetry of this situation, so now I have to find a use for the Caps Lock key alone. I have it mapped to `Esc`, a key that is used fairly often to cancel various operations and is also of heavy use in Emacs.

To summarize: when I just press the Caps Lock key, it acts like a `Escape` button. When I press the `Return` key, it acts like a `Return` key. When these two keys are kept pressed and used with conjunction with another key, they behave like a `Ctrl` key.


### Hyper key

You may ask: what do you do with the regular `Ctrl` keys? In the MacBook, there is no right `Ctrl` key, so I don't use it at all even in the Microsft keyboards (so that I can transition between keyboards as smootlhy as possible). The left `Ctrl` key, on both keyboards, is mapped to the so-called *Hyper* key, an incredible idea I stole from [Steve Losh](http://stevelosh.com/blog/2012/10/a-modern-space-cadet/ ).

The idea is that many programs in OS X make use of up three modifier keys. There are the standard `Cmd-C` to copy and `Cmd-V` to paste. In [Skim](http://thermocode.net/blog/skim2md), for example, to show a sidebard with the contents you press `Cmd-Shift-T`. In the Finder, you can invoke a "Go To..." dialog with `Cmd-Shift-G`. But no program use the four available modifier keys, like `Cmd-Shift-Option-Ctrl-<something>`, because that would be impossible to type. That's why I've remapped my left Control key to the Hyper key, which emulates the four modifiers. I use this key for "global" macros, like those created in Keyboard Maestro or enabled in some apps's preferences, since they don't conflict with any application-specific shortcuts. For example, `Hyper-L` triggers the [Fantastical](http://flexibits.com/fantastical ) 
 window. `Hyper-E` triggers a Keyboard Maestro macro that activate Emacs and hides all other applications, allowing me to easily focus on writing something.

I know, it's a bit complex, but it makes a lot of sense and really speeds things up.

### Setup

Here's how I set this up.

Under the *Keyboard* panel of *System Preferences*, in the keyboard tab, click on *Modifier Keys*:

![Keyboard preference pane]({filename}/images/keyboard-pane.png)

and change the "Caps Lock" menu to Control. You need to do this for every keyboard you use.

![Change Caps Lock Key]({filename}/images/remap-caps-lock.png)

For the other crazier remappings, I use two apps: [Seil](https://pqrs.org/osx/karabiner/seil.html.en ) 
 (for modifying individual keys) and [Karabiner](https://pqrs.org/osx/karabiner/index.html.en ) 
 (general remapping).

In Seil, remap the `Control_L` key to 80 (this is the 'F19' key, which don't even exist in many keyboards so it doesn't conflict with anything).

![Remap Control_L in Seil]({filename}/images/seil-controlL.png)

Now the left `Ctrl` key, the one I remap to that *Hyper* key, is acting like a F19 key, which does not do anything -- yet.

In Karabiner, under *Misc & Uninstall*, click to open the xml file

![Karabiner open private.xml]({filename}/images/karabiner-private-xml.png)

and add the following text:

	:::XML  
	<item>
		<name>Remap Left Control to Hyper</name>
		<appendix>OS X doesn't have a Hyper. This maps Left Control to Control + Shift + Option + Command.</appendix>
	
		<identifier>space_cadet.left_control_to_hyper</identifier>
	
		<autogen>
			--KeyToKey--
			KeyCode::F19,
	
			KeyCode::COMMAND_L,
			ModifierFlag::OPTION_L | ModifierFlag::SHIFT_L | ModifierFlag::CONTROL_L
		</autogen>
	</item>


This sets a `F19` key (which is bound to our left `Ctrl` key, remember) to the `Cmd` key, with the other three modifiers.

Now, in the *Change Key* tab, click on *Reload XML* you have to modify three settings: (you can search for them).

![Karabiner change keys]({filename}/images/karabiner-change-key.png)

Check the [Steve Losh post](http://stevelosh.com/blog/2012/10/a-modern-space-cadet/ ) for a more extensive explanation.

I'm crazy, but as [Carsten Dominik said](http://orgmode.org/talks/GoogleTech.html ), I like to make my computer work *exactly how I want it to work*.

## On Windows

All of this configuration is for OS X, which is the system I use the most. But I like it so much that I came up with a solution for Windows: [HomeCtrl](https://github.com/fabiofortkamp/homectrl ), an [AutoHotKey](http://ahkscript.org ) script. It does not provide a *Hyper* key yet, but the other configurations work. Check that page for more details.



