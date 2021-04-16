from abc import ABC, abstractmethod


class Data(ABC):
    """
    Abstract architecture to allow arbitrary datasets, which are provided by the user.
    """

    @property
    @abstractmethod
    def categoricals(self):
        """
        Provides the column names of categorical data.
        Column names do not contain encoded information as provided by a get_dummy() method (e.g., sex_female)

        Label name is not included.

        Returns
        -------
        list : List of Strings
            List of all categorical columns
        """
        pass

    @property
    @abstractmethod
    def continous(self):
        """
        Provides the column names of continuous data.

        Label name is not included.

        Returns
        -------
        list : List of Strings
            List of all continuous columns
        """
        pass

    @property
    @abstractmethod
    def immutables(self):
        """
        Provides the column names of immutable data.

        Label name is not included.

        Returns
        -------
        list : List of Strings
            List of all immutable columns
        """
        pass

    @property
    @abstractmethod
    def target(self):
        """
        Provides the name of the label column.

        Returns
        -------
        String : String
            Target label name
        """
        pass

    @property
    @abstractmethod
    def raw(self):
        """
        The raw Dataframe without encoding or normalization

        Returns
        -------
        df : :class:`pandas.DataFrame`
            Tabular data with raw information
        """
        pass

    @property
    @abstractmethod
    def normalized(self):
        """
        The normalized Dataframe without encoding

        Type of normalization can be arbitrary

        Returns
        -------
        df : :class:`pandas.DataFrame`
            Tabular data with normalized information
        """
        pass

    @property
    @abstractmethod
    def encoded(self):
        """
        The encoded Dataframe without normalization

        Type of encoding can be arbitrary

        Returns
        -------
        df : :class:`pandas.DataFrame`
            Tabular data with encoded information
        """
        pass

    @property
    @abstractmethod
    def encoded_normalized(self):
        """
        The normalized and encoded Dataframe

        Type of normalization and encoding have to be the same as for normalized and encoded

        Returns
        -------
        df : :class:`pandas.DataFrame`
            Tabular data with normalized and encoded information
        """
        pass
