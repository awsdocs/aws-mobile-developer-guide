# -*- coding: utf-8 -*-
#
# AWS Sphinx configuration file.
#
# For more information about how to configure this file, see:
#
# https://w.amazon.com/index.php/AWSDevDocs/Sphinx
#

#
# General information about the project.
#

# Optional service/SDK name, typically the three letter acronym (TLA) that
# represents the service, such as 'SWF'. If this is an SDK, you can use 'SDK'
# here.
service_name = u'Mobile'

# The long version of the service or SDK name, such as "Amazon Simple Workflow
# Service", "AWS Flow Framework for Ruby" or "AWS SDK for Java"
service_name_long = u'AWS ' + service_name

# The landing page for the service documentation.
service_docs_home = u'http://aws.amazon.com/documentation/aws-mobile/'

project = u'AWS Mobile Developer Guide'

# A short description of the project.
project_desc = u'%s %s' % (service_name_long, project)

# the output will be generated in latest/<project_basename> and will appear on
# the web using the same basename.
project_basename = 'mobile/aws-mobile/developerguide'

# This name is used as the manual / PDF name. Don't include the extension
# (.pdf) here.
man_name = 'aws-mobile-dg'

# The language for this version of the docs. Typically 'en'. For a full list of
# values, see: http://sphinx-doc.org/config.html#confval-language
language = u'en'

# Whether or not to show the PDF link. If you generate a PDF for your
# documentation, set this to True.
show_pdf_link = True

# Whether or not to show the language selector
show_lang_selector = True

# The link to the top of the doc source tree on GitHub. This allows generation
# of per-page "Edit on GitHub" links.
github_doc_url = 'https://github.com/awsdocs/aws-mobile-developer-guide/tree/master/doc_source'

#
# Version Information
#

# The version info for the project you're documenting, acts as replacement for
# |version| and |release| substitutions in the documentation, and is also used
# in various other places throughout the built documents.

# The short X.Y version.
version = '0.0.1'

# The full version, including alpha/beta/rc tags.
release = '0.0.1'

#
# Forum Information
#

# Optional forum ID. If there's a relevant forum at forums.aws.amazon.com, then
# set the ID here. If not set, then no forum ID link will be generated.
#forum_id = '88'

#
# Navlinks
#

# Extra navlinks. You can specify additional links to appear in the top bar here
# as navlink name / url pairs. If extra_navlinks is not set, then no extra
# navlinks will be generated.
#
# extra_navlinks = [
#         ('API Reference', 'http://path/to/api/reference'),
#         ('GitHub', 'http://path/to/github/project'),
#         ]
#extra_navlinks = [
#        ('API Reference', 'http://docs.aws.amazon.com/AWSiOSSDK/latest/'),
#        ('GitHub', 'https://github.com/aws/aws-sdk-ios'),
#        ('Samples', 'https://github.com/awslabs/aws-sdk-ios-samples'),
#        ('Download SDK',
#            'http://sdk-for-ios.amazonwebservices.com/latest/aws-ios-sdk.zip'),
    ]

build_html = True
build_pdf = True #Or False if you don't build a pdf
build_mobi = False #Or the Kindle ASIN if you need a Kindle build

feedback_name = 'Mobile SDK Docs'

# For the url docs.aws.amazon.com/docset-root/version/guide-name
docset_path_slug = 'mobile'
version_path_slug = 'aws-mobile'
guide_path_slug = 'developerguide'

#
# EXTRA_CONF_CONTENT -- don't change, move or remove this line!
#
# Any settings *below* this act as overrides for the default config content.
# Declare extlinks <http://sphinx-doc.org/latest/ext/extlinks.html> and
# additional configuration details specific to this documentation set here.

if 'extlinks' not in vars():
    extlinks = {}

# The feedback name is different than the service name...
html_theme_options = {} #['feedback_name'] = u'Mobile SDK Docs'

#-- Intersphinx mappings ------------------------------------------------------

# Mappings are used if you have more than one doc set that you'd like to refer
# to. The syntax is generally::
#
#  intersphinx_mapping = { 'mapname' : ('url', None) }
#
# For more information about intersphinx mappings, see:
#
# * http://sphinx-doc.org/latest/ext/intersphinx.html
#
aws_docs_url = 'http://' + aws_domains['documentation']
intersphinx_mapping = {
        'sdkforandroid': (aws_docs_url + '/mobile/sdkforandroid/developerguide', None),
#        'sdkforios': (aws_docs_url + '/mobile/sdkforios/developerguide', None),
        'sdkforunity': (aws_docs_url + '/mobile/sdkforunity/developerguide', None),
        'sdkforxamarin': (aws_docs_url + '/mobile/sdkforxamarin/developerguide', None),
        }

extlinks.update({
    # links to API pages or other non-standard guide links.
    'pol-dg': (aws_docs_url + '/lex/latest/developerguide/%s.html', ''),
    'lex-dg': (aws_docs_url + '/polly/latest/dg/%s.html', '')
})
