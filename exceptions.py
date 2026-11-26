class CatalogError(Exception):
    pass

class InvalidClassroomError(CatalogError):
    pass

class DuplicateClassroomError(CatalogError):
    pass

class ClassroomNotFoundError(CatalogError):
    pass

class UnsupportedFormatVersionError(CatalogError):
    pass

class InvalidCatalogFileError(CatalogError):
    pass