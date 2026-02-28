"""Visitor module."""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List


# pylint: disable=too-few-public-methods
class DocumentVisitor(ABC):
    """
    Abstract base class for document visitors.

    This class defines the visitor interface for processing different types of documents.
    Each concrete visitor must implement methods for visiting each document type.
    """

    @abstractmethod
    def visit_email(self, email: "Email") -> str:
        """
        Visit an Email document.

        Args:
            email (Email): The email document to process.

        Returns:
            str: Processing result for the email.
        """

    @abstractmethod
    def visit_report(self, report: "Report") -> str:
        """
        Visit a Report document.

        Args:
            report (Report): The report document to process.

        Returns:
            str: Processing result for the report.
        """


class Document(ABC):
    """
    Abstract base class for all document types.

    This class defines the common interface for documents that can accept visitors.
    All concrete document types must implement the accept method.

    Attributes:
        title (str): The document title.
        created_date (datetime): When the document was created.
    """

    def __init__(self, title: str, created_date: datetime):
        """
        Initialize a document with a title and creation date.

        Args:
            title (str): The document title.
            created_date (datetime): When the document was created.
        """
        self.title = title
        self.created_date = created_date

    @abstractmethod
    def accept(self, visitor: DocumentVisitor) -> str:
        """
        Accept a visitor for processing this document.

        Args:
            visitor (DocumentVisitor): The visitor to process this document.

        Returns:
            str: Result of the visitor's processing.
        """


class Email(Document):
    """
    Represents an email document.

    Contains email-specific attributes like sender, recipients, and attachment count.

    Attributes:
        sender (str): Email sender address.
        recipients (List[str]): List of recipient addresses.
        attachment_count (int): Number of file attachments.
    """

    # pylint: disable=too-many-arguments
    def __init__(self, title: str, created_date: datetime, sender: str, recipients: List[str], attachment_count: int):
        """
        Initialize an email document.

        Args:
            title (str): The email subject.
            created_date (datetime): When the email was sent.
            sender (str): Email sender address.
            recipients (List[str]): List of recipient addresses.
            attachment_count (int): Number of file attachments.
        """
        super().__init__(title, created_date)
        self.sender = sender
        self.recipients = recipients
        self.attachment_count = attachment_count

    def accept(self, visitor: DocumentVisitor) -> str:
        """
        Accept a visitor for processing this email.

        Args:
            visitor (DocumentVisitor): The visitor to process this email.

        Returns:
            str: Result of the visitor's processing.
        """
        return visitor.visit_email(self)


class Report(Document):
    """
    Represents a business report document.

    Contains report-specific attributes like department, page count, and confidentiality.

    Attributes:
        department (str): The department that created the report.
        page_count (int): Number of pages in the report.
        confidential (bool): Whether the report contains confidential information.
    """

    # pylint: disable=too-many-arguments
    def __init__(self, title: str, created_date: datetime, department: str, page_count: int, confidential: bool):
        """
        Initialize a report document.

        Args:
            title (str): The report title.
            created_date (datetime): When the report was created.
            department (str): The department that created the report.
            page_count (int): Number of pages in the report.
            confidential (bool): Whether the report contains confidential information.
        """
        super().__init__(title, created_date)
        self.department = department
        self.page_count = page_count
        self.confidential = confidential

    def accept(self, visitor: DocumentVisitor) -> str:
        """
        Accept a visitor for processing this report.

        Args:
            visitor (DocumentVisitor): The visitor to process this report.

        Returns:
            str: Result of the visitor's processing.
        """
        return visitor.visit_report(self)


class SecurityScanner(DocumentVisitor):
    """
    Document a visitor that performs security risk assessment.

    Analyzes documents for potential security risks based on their characteristics
    and returns a security assessment report.
    """

    def visit_email(self, email: Email) -> str:
        """
        Perform a security scan on an email document.

        Evaluates risk based on attachment count, with more attachments indicating higher risk.

        Args:
            email (Email): The email document to scan.

        Returns:
            str: Security scan result with risk assessment.
        """
        risk_level = "HIGH" if email.attachment_count > 3 else "LOW"
        return f"Email security scan: Risk {risk_level} ({email.attachment_count} attachments)"

    def visit_report(self, report: Report) -> str:
        """
        Perform security scan on a report document.

        Evaluates risk based on confidentiality status, with confidential reports being critical.

        Args:
            report (Report): The report document to scan.

        Returns:
            str: Security scan result with risk assessment.
        """
        risk_level = "CRITICAL" if report.confidential else "NORMAL"
        return f"Report security scan: {risk_level} - Department: {report.department}"


class MetadataExtractor(DocumentVisitor):
    """
    Document visitor that extracts important metadata from documents.

    Collects key information from different document types to provide
    structured metadata summaries.
    """

    def visit_email(self, email: Email) -> str:
        """
        Extract metadata from an email document.

        Collects sender information, recipient count, and attachment count.

        Args:
            email (Email): The email document to extract metadata from.

        Returns:
            str: Formatted metadata summary for the email.
        """
        recipient_info = f"{len(email.recipients)} recipients"
        return f"Email metadata: From {email.sender}, {recipient_info}, {email.attachment_count} files"

    def visit_report(self, report: Report) -> str:
        """
        Extract metadata from a report document.

        Collects page count, department, and confidentiality status.

        Args:
            report (Report): The report document to extract metadata from.

        Returns:
            str: Formatted metadata summary for the report.
        """
        confidential_mark = " [CONFIDENTIAL]" if report.confidential else ""
        return f"Report metadata: {report.page_count} pages, {report.department}{confidential_mark}"


# Example usage
documents: List[Document] = [
    Email(
        "Q4 Project Meeting",
        datetime(2024, 1, 15),
        "manager@company.com",
        ["team@company.com", "external@partner.com"],
        5,
    ),
    Report("Financial Quarterly Report", datetime(2023, 12, 31), "Finance", 45, True),
]

# Apply different visitors
security_scanner = SecurityScanner()
metadata_extractor = MetadataExtractor()

for i, doc in enumerate(documents, 1):
    print(f"Document {i}: {doc.title}")
    print(f"  {doc.accept(security_scanner)}")
    print(f"  {doc.accept(metadata_extractor)}")
