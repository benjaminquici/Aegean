Aegean software tools
======

Programs included:
* aegean - The Aegean source finding program. All your^ radio astronomy source finding needs in one spiffy program.
* BANE - The Background and Noise Estimation tool. For providing high quality background and noise images for use with Aegean, at a small fraction of the cost of a full box-car smooth.
* MIMAS - The Multi-resolution Image Masking tool for Aegean Software. For creating image regions which can be used to restrict the source finding of Aegean, to mask fits files, and to create ds9 region files.
* SR6 - A tool for shrinking and growing fits files, such as those created with BANE.py --compress. Shrinking is done by decimation, growing is done by linear interpolation.

^ - by "your" I mean "my"

Installing
=====
AegeanTools is guaranteed to work on python 2.7. Earlier versions will often work, but 3.0 is not (yet) supported.

You can install via pip using 
`pip install git+https://github.com/PaulHancock/Aegean.git` (latest)
`pip install AegeanTools` (stable)

Or you can clone or download the repository and then use `python setup.py install`

Help
=====
Please see the [wiki pages](https://github.com/PaulHancock/Aegean/wiki) for some help and examples. If you have questions that are not answerd in the wiki please feel free to email me. If you have found a bug or some inconsistency in the code please [submit a ticket](https://github.com/PaulHancock/Aegean/issues) (which will trigger an email to me) and I'll get right on it. 

Credit
=====
If you use Aegean or any of the AegeanTools for your research please credit me by citing [Hancock et al 2012, MNRAS, 422, 1812](http://adsabs.harvard.edu/abs/2012MNRAS.422.1812H), Hancock et al 2017 (submitted).

Until there is a more appropriate method for crediting software development and maintainance, please also consider including me as a co-author on publications which rely on Aegean or AegeanTools.


Status
=====
[![Build Status](https://travis-ci.org/PaulHancock/Aegean.svg?branch=six)](https://travis-ci.org/PaulHancock/Aegean) [![Coverage Status](https://coveralls.io/repos/github/PaulHancock/Aegean/badge.svg?branch=six)](https://coveralls.io/github/PaulHancock/Aegean?branch=six)

