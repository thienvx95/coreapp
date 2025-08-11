from app.core.logging import logger
import os

class FileReaderService:
    """
    A simple service to read files.
    """

    def __init__(self):
        """
        Initializes the FileReaderService.
        """
        pass

    @staticmethod
    def read_file(file_path: str) -> str | None:
        """
        Reads the content of a file.

        Args:
            file_path: The absolute or relative path to the file.

        Returns:
            The content of the file as a string, or None if an error occurs.
        """
        try:
            # Check if the file path is valid and the file exists
            if not os.path.exists(file_path):
                logger.error(f"Error: File not found at path: {file_path}")
                return None
            if not os.path.isfile(file_path):
                logger.error(f"Error: Path provided is a directory, not a file: {file_path}")
                return None

            # Open and read the file
            # 'with' statement ensures the file is properly closed even if errors occur
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            # This exception is technically covered by os.path.exists,
            # but it's good practice to include it for open()
            logger.error(f"Error: File not found at path: {file_path}")
            return None
        except PermissionError:
            logger.error(f"Error: Permission denied to read the file: {file_path}")
            return None
        except UnicodeDecodeError:
            logger.error(f"Error: Could not decode the file with UTF-8 encoding. The file might be binary or use a different encoding: {file_path}")
            return None
        except IOError as e:
            # Handles other I/O related errors
            logger.error(f"An I/O error occurred: {e}")
            return None
        except Exception as e:
            # Catch any other unexpected errors
            logger.error(f"An unexpected error occurred: {e}")
            return None
