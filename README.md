# stderr_suppression
Because sometimes warning filters aren't enough, and because I'm a terrible person.

This code originated when I was working on hiveplotter: every time a plot was shown or saved, PyX would produce about 20 lines of warnings which couldn't be caught by the warnings module. This redirects any stderr output matching a particular regex to an object with a null write() method, and any others to stderr.
