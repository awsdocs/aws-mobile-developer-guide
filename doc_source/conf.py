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

# sphinx-build constants
extensions = ['sphinx.ext.extlinks']

master_doc = 'index'


# Optional service/SDK name, typically the three letter acronym (TLA) that
# represents the service, such as 'SWF'. If this is an SDK, you can use 'SDK'
# here.
service_name = "AWS Mobile"

# The long version of the service or SDK name, such as "Amazon Simple Workflow
# Service", "AWS Flow Framework for Ruby" or "AWS SDK for Java"
service_name_long = u'AWS Mobile'

# The landing page for the service documentation.
service_docs_home = u'https://aws.amazon.com/documentation/aws-mobile/'

# The project type, such as "Developer Guide", "API Reference", "User Guide",
# or whatever.
project = u'Developer Guide'

# A short description of the project.
project_desc = "AWS Mobile Developer Guide"

# the output will be generated in latest/<project_basename> and will appear on
# the web using the same basename.
project_basename = 'DeveloperGuide'

# This name is used as the manual / PDF name. Don't include the extension
# (.pdf) here.
man_name = 'aws-mobile-dg'

# The language for this version of the docs. Typically 'en'. For a full list of
# values, see: http://sphinx-doc.org/config.html#confval-language
language = u'en'

# Whether or not to show the PDF link. If you generate a PDF for your
# documentation, set this to True.
show_pdf_link = True

# Don't show the language selector (yet)
show_lang_selector = True

# The link to the top of the doc source tree on GitHub. This allows generation
# of per-page "Edit on GitHub" links.
github_doc_url = 'https://github.com/awsdocs/aws-mobile-developer-guide/tree/master/doc_source'

# This allows the "Feedback" button to create a new issue on GitHub.
#doc_feedback_url = 'https://github.com/awsdocs/aws-java-developer-guide/issues/new'
feedback_name = u'AWS Mobile'
#feedback_folder_id = 'b8effc8e-3e23-4650-bf44-51b6b56ebce3'
feedback_folder_id = 'e2dc4143-f728-4878-a1b6-cab44164e948'

#
# Version Information
#

# The version info for the project you're documenting, acts as replacement for
# |version| and |release| substitutions in the documentation, and is also used
# in various other places throughout the built documents.
#
# The short X.Y version.

version = '1.0'

# The full version, including alpha/beta/rc tags.

release = '1.0'


#
# Forum Information
#

# Optional forum ID. If there's a relevant forum at forums.aws.amazon.com, then
# set the ID here. If not set, then no forum ID link will be generated.
#

#forum_id = '70'

#
# Extra Navlinks
#

# Extra navlinks. You can specify additional links to appear in the top bar here
# as navlink name / url pairs. If extra_navlinks is not set, then no extra
# navlinks will be generated.
#
extra_navlinks = [
#         ('API Reference', 'http://path/to/api/reference'),
        ('GitHub', 'https://github.com/awsdocs/aws-mobile-developer-guide'),
         ]

# Extra navlinks. You can specify additional links to appear in the top bar here
# as navlink name / url pairs. If extra_navlinks is not set, then no extra
# navlinks will be generated.
# THIS DOESN'T CURRENTLY WORK IN Sphinx to Zonbook - kept for reference and perhaps future use
extra_navlinks = [
        ('Android API Reference', 'http://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/'),
        ('GitHub (Android)', 'https://github.com/aws/aws-sdk-android'),
        ('Samples (Android)', 'https://github.com/awslabs/aws-sdk-android-samples'),
        ('Download SDK(Android)', 'http://sdk-for-android.amazonwebservices.com/latest/aws-android-sdk.zip'),
        ('iOS API Reference', 'http://docs.aws.amazon.com/AWSiOSSDK/latest/'),
        ('GitHub (iOS)', 'https://github.com/aws/aws-sdk-ios'),
        ('Samples (iOS)', 'https://github.com/awslabs/aws-sdk-ios-samples')
    ]


build_html = True
build_pdf = True # Or False if you don't build a pdf
build_mobi = False # Or the Kindle ASIN if you need a Kindle build

feedback_name = 'Mobile SDK Docs'

# For the url docs.aws.amazon.com/docset-root/version/guide-name
docset_path_slug = 'aws-mobile'
version_path_slug = 'latest'
guide_path_slug = 'developerguide'

#
# EXTRA_CONF_CONTENT -- don't change, move or remove this line!
#
# Any settings *below* this act as overrides for the default config content.
# Declare extlinks <http://sphinx-doc.org/latest/ext/extlinks.html> and
# additional configuration details specific to this documentation set here.
#

# add rss feed generation.
# extensions.append('sphinxcontrib.newsfeed')

# default code language for syntax highlighting
#highlight_language = 'java'

if 'extlinks' not in vars():
    extlinks = {}

# extlinks['role'] = (url_string, term_prepended_by)

