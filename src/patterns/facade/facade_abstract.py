"""Facade module."""

from abc import ABC, abstractmethod

# pylint: disable=too-few-public-methods


class DeploymentFacade(ABC):
    """Abstract facade for deployment operations."""

    @abstractmethod
    def deploy(self, version: str) -> str:
        """
        Deploy a specific version.

        Args:
            version: Version string to deploy.

        Returns:
            Deployment result message.
        """


class CIServer:
    """Continuous Integration server for running tests."""

    @staticmethod
    def run_tests() -> str:
        """
        Run all tests.

        Returns:
            Test execution result.
        """
        return "CI: All tests passed"


class ContainerRegistry:
    """Container registry for building and pushing images."""

    @staticmethod
    def build_and_push(version: str) -> str:
        """
        Build and push container image.

        Args:
            version: Version tag for the image.

        Returns:
            Build and push a result message.
        """
        return f"Registry: Built and pushed image v{version}"


class Orchestrator:
    """Container orchestrator for managing deployments."""

    @staticmethod
    def rolling_update(version: str) -> str:
        """
        Perform rolling update deployment.

        Args:
            version: Version to deploy.

        Returns:
            Rolling update result message.
        """
        return f"Orchestrator: Rolling update to v{version} complete"


class ProductionDeploymentFacade(DeploymentFacade):
    """Production deployment facade that coordinates multiple systems."""

    def __init__(self) -> None:
        """Initialize production deployment facade with required services."""
        self._ci = CIServer()
        self._registry = ContainerRegistry()
        self._orchestrator = Orchestrator()

    def deploy(self, version: str) -> str:
        """
        Deploy version to production environment.

        Args:
            version: Version string to deploy.

        Returns:
            Complete deployment process output.
        """
        steps = [
            f"Starting deployment of v{version}...",
            self._ci.run_tests(),
            self._registry.build_and_push(version),
            self._orchestrator.rolling_update(version),
            "Deployment successful!",
        ]
        return "\n".join(steps)


class MockDeploymentFacade(DeploymentFacade):
    """Mock deployment facade for testing purposes."""

    def deploy(self, version: str) -> str:
        """
        Simulate deployment process.

        Args:
            version: Version string to simulate deploying.

        Returns:
            Mock deployment message.
        """
        return f"Mock: Simulated deployment of v{version}"


# Client code works with the abstraction
def run_deployment(facade: DeploymentFacade, version: str) -> None:
    """
    Execute deployment using the provided facade.

    Args:
        facade: Deployment facade implementation to use.
        version: Version string to deploy.
    """
    print(facade.deploy(version))


run_deployment(ProductionDeploymentFacade(), "2.4.1")
run_deployment(MockDeploymentFacade(), "2.4.1")
