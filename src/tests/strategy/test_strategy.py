"""Test strategy module."""

import bz2
import zlib
from io import StringIO
from unittest.mock import patch

from patterns.strategy.strategy import (
    Bz2Compression,
    FileProcessor,
    NoCompression,
    ZipCompression,
)


class TestCompressionStrategies:
    """
    Test cases for the compression strategy implementations.
    """

    test_data = b"""Lorem ipsum dolor sit amet, consetetur sadipscing elitr,
                sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
                sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum."""

    def test_zip_compression_name(self) -> None:
        """
        Test that ZipCompression returns the correct name.

        Returns:
            None
        """
        strategy = ZipCompression()
        assert strategy.name() == "ZIP"

    def test_zip_compression_compress(self) -> None:
        """
        Test that ZipCompression compresses data correctly.

        Returns:
            None
        """
        strategy = ZipCompression()

        compressed = strategy.compress(self.test_data)
        decompressed = zlib.decompress(compressed)

        assert decompressed == self.test_data
        assert len(compressed) < len(self.test_data)

    def test_bz2_compression_name(self) -> None:
        """
        Test that Bz2Compression returns the correct name.

        Returns:
            None
        """
        strategy = Bz2Compression()
        assert strategy.name() == "BZ2"

    def test_bz2_compression_compress(self) -> None:
        """
        Test that Bz2Compression compresses data correctly.

        Returns:
            None
        """
        strategy = Bz2Compression()

        compressed = strategy.compress(self.test_data)
        decompressed = bz2.decompress(compressed)

        assert decompressed == self.test_data
        assert len(compressed) <= len(self.test_data)

    def test_no_compression_name(self) -> None:
        """
        Test that NoCompression returns the correct name.

        Returns:
            None
        """
        strategy = NoCompression()
        assert strategy.name() == "NONE"

    def test_no_compression_compress(self) -> None:
        """
        Test that NoCompression returns data unchanged.

        Returns:
            None
        """
        strategy = NoCompression()

        result = strategy.compress(self.test_data)

        assert result == self.test_data
        assert len(result) == len(self.test_data)


class TestFileProcessor:
    """
    Test cases for the FileProcessor class.
    """

    test_data = b"""Lorem ipsum dolor sit amet, consetetur sadipscing elitr,
                    sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
                    sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum."""

    # pylint: disable=protected-access
    def test_file_processor_initialization(self) -> None:
        """
        Test that FileProcessor initializes correctly with a strategy.

        Returns:
            None
        """
        strategy = ZipCompression()
        processor = FileProcessor(strategy)

        assert processor._strategy == strategy

    # pylint: disable=protected-access
    def test_file_processor_set_strategy(self) -> None:
        """
        Test that FileProcessor can change strategies at runtime.

        Returns:
            None
        """
        initial_strategy = ZipCompression()
        new_strategy = Bz2Compression()
        processor = FileProcessor(initial_strategy)

        processor.set_strategy(new_strategy)

        assert processor._strategy == new_strategy

    @patch("sys.stdout", new_callable=StringIO)
    def test_file_processor_process_with_zip(self, mock_stdout) -> None:
        """
        Test FileProcessor process method with ZIP compression.

        Args:
            mock_stdout: Mocked stdout for capturing print output

        Returns:
            None
        """
        strategy = ZipCompression()
        processor = FileProcessor(strategy)

        result = processor.process(self.test_data)
        output = mock_stdout.getvalue()

        assert len(result) < len(self.test_data)
        assert "Processing with ZIP compression..." in output
        assert f"Original: {len(self.test_data)} bytes" in output

    @patch("sys.stdout", new_callable=StringIO)
    def test_file_processor_process_with_no_compression(self, mock_stdout) -> None:
        """
        Test FileProcessor process method with no compression.

        Args:
            mock_stdout: Mocked stdout for capturing print output

        Returns:
            None
        """
        strategy = NoCompression()
        processor = FileProcessor(strategy)

        result = processor.process(self.test_data)
        output = mock_stdout.getvalue()

        assert result == self.test_data
        assert "Processing with NONE compression..." in output
        assert "100.0%" in output

    @patch("sys.stdout", new_callable=StringIO)
    def test_file_processor_compression_ratio_calculation(self, mock_stdout) -> None:
        """
        Test that FileProcessor calculates the compression ratio correctly.

        Args:
            mock_stdout: Mocked stdout for capturing print output

        Returns:
            None
        """
        strategy = NoCompression()
        processor = FileProcessor(strategy)
        test_data = b"1234567890"  # 10 bytes

        processor.process(test_data)
        output = mock_stdout.getvalue()

        assert "100.0%" in output
        assert "10 bytes -> Compressed: 10 bytes" in output


class TestStrategyPattern:
    """
    Test cases for the Strategy Pattern implementation.
    """

    test_data = b"""Lorem ipsum dolor sit amet, consetetur sadipscing elitr,
                    sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
                    sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum."""

    def test_strategy_pattern_polymorphism(self) -> None:
        """
        Test that different strategies can be used polymorphically.

        Returns:
            None
        """
        strategies = [ZipCompression(), Bz2Compression(), NoCompression()]

        results = []
        for strategy in strategies:
            processor = FileProcessor(strategy)
            results.append(processor.process(self.test_data))

        assert all(isinstance(result, bytes) for result in results)
        assert len(set(len(result) for result in results)) >= 2

    def test_strategy_switching_runtime(self) -> None:
        """
        Test that strategies can be switched at runtime.

        Returns:
            None
        """
        processor = FileProcessor(ZipCompression())

        zip_result = processor.process(self.test_data)

        processor.set_strategy(Bz2Compression())
        bz2_result = processor.process(self.test_data)

        processor.set_strategy(NoCompression())
        none_result = processor.process(self.test_data)

        assert zip_result != bz2_result
        assert bz2_result != none_result
        assert none_result == self.test_data

    def test_empty_data_handling(self) -> None:
        """
        Test that all strategies handle empty data correctly.

        Returns:
            None
        """
        strategies = [ZipCompression(), Bz2Compression(), NoCompression()]
        empty_data = b""

        for strategy in strategies:
            result = strategy.compress(empty_data)
            assert isinstance(result, bytes)

    def test_large_data_compression(self) -> None:
        """
        Test compression strategies with larger data sets.

        Returns:
            None
        """
        large_data = self.test_data * 1000  # about 248KB

        zip_strategy = ZipCompression()
        bz2_strategy = Bz2Compression()
        none_strategy = NoCompression()

        zip_result = zip_strategy.compress(large_data)
        bz2_result = bz2_strategy.compress(large_data)
        none_result = none_strategy.compress(large_data)

        assert len(zip_result) < len(large_data)
        assert len(bz2_result) < len(large_data)
        assert len(none_result) == len(large_data)
