"""Test visitor module."""

from datetime import datetime

from patterns.visitor.visitor import Email, MetadataExtractor, Report, SecurityScanner


class TestDocumentClasses:
    """
    Test cases for the Document classes implementation.
    """

    def test_email_creation_and_attributes(self) -> None:
        """
        Test that Email objects are created correctly with all attributes.

        Returns:
            None
        """
        created_date = datetime(2024, 1, 15)
        recipients = ["user1@test.com", "user2@test.com"]

        email = Email("Test Subject", created_date, "sender@test.com", recipients, 3)

        assert email.title == "Test Subject"
        assert email.created_date == created_date
        assert email.sender == "sender@test.com"
        assert email.recipients == recipients
        assert email.attachment_count == 3

    def test_report_creation_and_attributes(self) -> None:
        """
        Test that Report objects are created correctly with all attributes.

        Returns:
            None
        """
        created_date = datetime(2023, 12, 31)

        report = Report("Annual Report", created_date, "Finance", 100, True)

        assert report.title == "Annual Report"
        assert report.created_date == created_date
        assert report.department == "Finance"
        assert report.page_count == 100
        assert report.confidential is True


class TestVisitorPattern:
    """
    Test cases for the implementation of the Visitor Pattern.
    """

    def test_security_scanner_email_low_risk(self) -> None:
        """
        Test SecurityScanner with low-risk email (3 or fewer attachments).

        Returns:
            None
        """
        email = Email("Safe Email", datetime(2024, 1, 1), "sender@test.com", ["recipient@test.com"], 2)
        scanner = SecurityScanner()

        result = email.accept(scanner)

        assert result == "Email security scan: Risk LOW (2 attachments)"

    def test_security_scanner_email_high_risk(self) -> None:
        """
        Test SecurityScanner with high-risk email (more than 3 attachments).

        Returns:
            None
        """
        email = Email("Suspicious Email", datetime(2024, 1, 1), "sender@test.com", ["recipient@test.com"], 5)
        scanner = SecurityScanner()

        result = email.accept(scanner)

        assert result == "Email security scan: Risk HIGH (5 attachments)"

    def test_security_scanner_report_normal_risk(self) -> None:
        """
        Test SecurityScanner with normal report (not confidential).

        Returns:
            None
        """
        report = Report("Public Report", datetime(2024, 1, 1), "Marketing", 25, False)
        scanner = SecurityScanner()

        result = report.accept(scanner)

        assert result == "Report security scan: NORMAL - Department: Marketing"

    def test_security_scanner_report_critical_risk(self) -> None:
        """
        Test SecurityScanner with critical report (confidential).

        Returns:
            None
        """
        report = Report("Confidential Report", datetime(2024, 1, 1), "HR", 50, True)
        scanner = SecurityScanner()

        result = report.accept(scanner)

        assert result == "Report security scan: CRITICAL - Department: HR"

    def test_metadata_extractor_email(self) -> None:
        """
        Test MetadataExtractor with email document.

        Returns:
            None
        """
        email = Email(
            "Team Meeting",
            datetime(2024, 1, 1),
            "manager@company.com",
            ["dev1@company.com", "dev2@company.com", "qa@company.com"],
            2,
        )
        extractor = MetadataExtractor()

        result = email.accept(extractor)

        assert result == "Email metadata: From manager@company.com, 3 recipients, 2 files"

    def test_metadata_extractor_report_non_confidential(self) -> None:
        """
        Test MetadataExtractor with non-confidential report.

        Returns:
            None
        """
        report = Report("Sales Report", datetime(2024, 1, 1), "Sales", 15, False)
        extractor = MetadataExtractor()

        result = report.accept(extractor)

        assert result == "Report metadata: 15 pages, Sales"

    def test_metadata_extractor_report_confidential(self) -> None:
        """
        Test MetadataExtractor with confidential report.

        Returns:
            None
        """
        report = Report("Internal Audit", datetime(2024, 1, 1), "Audit", 75, True)
        extractor = MetadataExtractor()

        result = report.accept(extractor)

        assert result == "Report metadata: 75 pages, Audit [CONFIDENTIAL]"

    def test_visitor_pattern_polymorphism(self) -> None:
        """
        Test that different document types accept visitors correctly.

        Returns:
            None
        """
        documents = [
            Email("Email Doc", datetime(2024, 1, 1), "test@test.com", ["user@test.com"], 1),
            Report("Report Doc", datetime(2024, 1, 1), "IT", 10, False),
        ]

        scanner = SecurityScanner()
        results = [doc.accept(scanner) for doc in documents]

        assert "Email security scan" in results[0]
        assert "Report security scan" in results[1]

    def test_multiple_visitors_same_document(self) -> None:
        """
        Test that the same document can accept multiple different visitors.

        Returns:
            None
        """
        email = Email("Multi-visitor Test", datetime(2024, 1, 1), "sender@test.com", ["recipient@test.com"], 4)

        scanner = SecurityScanner()
        extractor = MetadataExtractor()

        security_result = email.accept(scanner)
        metadata_result = email.accept(extractor)

        assert "Email security scan: Risk HIGH" in security_result
        assert "Email metadata: From sender@test.com" in metadata_result
