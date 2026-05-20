from abc import ABC,abstractmethod
from schema import Report

class IReportGenerator(ABC):
  
  @abstractmethod
  def generate_report(self,report:Report):
    pass
  