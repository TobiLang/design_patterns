"""Visitor module."""

import bz2
import zlib
from abc import ABC, abstractmethod


class CompressionStrategy(ABC):
    """Compression strategy interface."""

    @abstractmethod
    def compress(self, data: bytes) -> bytes:
        """
        Compress the given data using the strategy.

        Args:
            data (bytes): The data to compress.

        Returns:
            A compressed version of the input data.
        """

    @abstractmethod
    def name(self) -> str:
        """Return the name of the strategy."""


class ZipCompression(CompressionStrategy):
    """Zip compression strategy."""

    def compress(self, data: bytes) -> bytes:
        """
        Compress the given data using the ZIP algorithm.

        Args:
            data (bytes): The data to compress.

        Returns:
            Zip compressed data.
        """

        return zlib.compress(data)

    def name(self) -> str:
        """Return the name of the strategy."""
        return "ZIP"


class Bz2Compression(CompressionStrategy):
    """Bz2 compression strategy."""

    def compress(self, data: bytes) -> bytes:
        """
        Compress the given data using the BZ2 algorithm.

        Args:
            data (bytes): The data to compress.

        Returns:
            BZ2 compressed data.
        """
        return bz2.compress(data)

    def name(self) -> str:
        """Return the name of the strategy."""
        return "BZ2"


class NoCompression(CompressionStrategy):
    """No compression strategy."""

    def compress(self, data: bytes) -> bytes:
        """
        Return the original data without compression.

        Args:
            data (bytes): The data to compress.

        Returns:
            The original data.
        """
        return data

    def name(self) -> str:
        """Return the name of the strategy."""
        return "NONE"


class FileProcessor:
    """File processor class that uses a compression strategy."""

    def __init__(self, strategy: CompressionStrategy) -> None:
        """
        Initialize the FileProcessor with a compression strategy.

        Args:
            strategy (CompressionStrategy): The compression strategy to use.
        """
        self._strategy = strategy

    def set_strategy(self, strategy: CompressionStrategy) -> None:
        """
        Set the compression strategy to use.

        Args:
            strategy (CompressionStrategy): The compression strategy to use.
        """
        self._strategy = strategy

    def process(self, data: bytes) -> bytes:
        """
        Process the given data using the compression strategy.

        Args:
            data (bytes): The data to compress.

        Returns:
            A compressed version of the input data.
        """
        print(f"Processing with {self._strategy.name()} compression...")
        compressed = self._strategy.compress(data)
        ratio = len(compressed) / len(data) * 100
        print(f"  Original: {len(data)} bytes -> Compressed: {len(compressed)} bytes ({ratio:.1f}%)")
        return compressed
