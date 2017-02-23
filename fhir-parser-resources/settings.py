# These are settings for the FHIR class generator.
# All paths are relative to the `fhir-parser` directory. You can use '/' to
# indicate directories: the parser will split them on '/' and use os.path to
# make them platform independent.

from Default.settings import *
from mappings import *

# Base URL for where to load specification data from
specification_url = 'http://build.fhir.org'

# In which directory to find the templates. See below for settings that start with `tpl_`: these are the template names.
tpl_base = '../fhir-parser-resources'

# Whether and where to put the generated class models
write_resources = True
tpl_resource_source = 'template-resource.swift'          # the template to use as source when writing resource implementations for profiles
tpl_resource_target = '../Sources/Models'                # target directory to write the generated class files to
tpl_resource_target_ptrn = '{}.swift'                    # where to write the generated class files to, with one "{}" placeholder for the class name
tpl_codesystems_source = 'template-codesystems.swift'    # the template to use as source when writing enums for CodeSystems; can be `None`
tpl_codesystems_target_name = 'CodeSystems.swift'        # the filename to use for the generated code systems and value sets (in `tpl_resource_target`)

# Whether and where to put the factory methods
write_factory = write_resources
tpl_factory_source = 'template-elementfactory.swift'                       # the template to use for factory generation
tpl_factory_target = '../Sources/Models/FHIRAbstractBase+Factory.swift'    # where to write the generated factory to

# Whether and where to write unit tests
write_unittests = True
tpl_unittest_source = 'template-unittest.swift'    # the template to use for unit test generation
tpl_unittest_target = '../Tests/ModelTests'        # target directory to write the generated unit test files to
tpl_unittest_target_ptrn = '{}Tests.swift'         # a pattern to determine the output files for unit tests; the one placeholder will be the class name
unittest_copyfiles = [                             # array of file names to copy to the test directory `tpl_unittest_target` (e.g. unit test base classes)
    '../fhir-parser-resources/XCTestCase+FHIR.swift',
    '../fhir-parser-resources/DateAndTimeTests.swift',
]

unittest_format_path_prepare = '{}?'      # used to format `path` before appending another path element - one placeholder for `path`
unittest_format_path_key = '{}.{}'        # used to create property paths by appending `key` to the existing `path` - two placeholders
unittest_format_path_index = '{}?[{}]'    # used for array properties - two placeholders, `path` and the array index

# Settings for classes and resources
resource_modules_lowercase = False        # whether all resource paths (i.e. modules) should be lowercase
camelcase_classes = True                  # whether class name generation should use CamelCase
camelcase_enums = True                    # whether names for enums should be camelCased
backbone_class_adds_parent = True         # if True, backbone class names prepend their parent's class name

# All these files should be copied to dirname(`tpl_resource_target_ptrn`): tuples of (path/to/file, module, array-of-class-names)
manual_profiles = [
    ('../fhir-parser-resources/FHIRAbstractBase.swift', None, ['FHIRAbstractBase']),
    ('../fhir-parser-resources/FHIRAbstractResource.swift', None, ['FHIRAbstractResource']),
    ('../fhir-parser-resources/FHIRPrimitive.swift', None, []),
    ('../fhir-parser-resources/FHIRType.swift', None, []),
    ('../fhir-parser-resources/FHIRString.swift', None, [
        'string', 'code', 'id', 'uuid', 'markdown', 'xhtml',
    ]),
    ('../fhir-parser-resources/FHIRURL.swift', None, [
        'uri', 'oid'
    ]),
    ('../fhir-parser-resources/DateAndTime.swift', None, [
        'date', 'dateTime', 'time', 'instant',
    ]),
    ('../fhir-parser-resources/Base64Binary.swift', None, [
        'base64Binary',
    ]),
    ('../fhir-parser-resources/FHIRBool.swift', None, [
        'boolean',
    ]),
    ('../fhir-parser-resources/FHIRDecimal.swift', None, [
        'decimal',
    ]),
    ('../fhir-parser-resources/FHIRInteger.swift', None, [
        'integer', 'positiveInt', 'unsignedInt',
    ]),
    ('../fhir-parser-resources/FHIREnum.swift', None, []),
    ('../fhir-parser-resources/FHIRRequest.swift', None, []),
    ('../fhir-parser-resources/FHIRRequestHandler.swift', None, []),
    ('../fhir-parser-resources/FHIRServer.swift', None, ['FHIRServer']),
    ('../fhir-parser-resources/FHIRServerResponse.swift', None, []),
    ('../fhir-parser-resources/FHIRError.swift', None, ['FHIRError']),
    ('../fhir-parser-resources/FHIRValidationError.swift', None, ['FHIRValidationError']),
]
