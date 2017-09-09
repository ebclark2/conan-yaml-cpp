from conans import ConanFile, CMake
import os

username = os.getenv( '"CONAN_USERNAME', 'ebclark2' )
channel = os.getenv( 'CONAN_CHANNEL', 'testing' )

class YamlCppTestConan( ConanFile ):
  settings = 'os', 'compiler', 'build_type', 'arch'
  requires = 'yaml-cpp/master@%s/%s' %  (username, channel )
  build_requires = "cmake_installer/1.0@conan/stable"
  generators = 'cmake'

  def build( self ):
    cmake = CMake(self)
    cmake.configure(source_dir=self.conanfile_directory)
    cmake.build()

  def imports( self ):
    self.copy( '*.dll', 'bin', 'bin' )
    self.copy( '*.dylib', 'bin', 'bin' )

  def test( self ):
    os.chdir( 'bin' )
    self.run( '.%sexample' % os.sep )
