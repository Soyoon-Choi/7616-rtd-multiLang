## Preface

### About This Manual

This manual explains the concepts, components, and basic use of Altibase.

#### Audience

This manual has been prepared for the following Altibase users:
  - Database managers
  - Performance managers
  - Database users
  - Application developers
  - Technical support engineers

It is recommended for those reading this manual possess the following background knowledge: 

- Basic knowledge in the use of computers, operating systems, and operating system utilities
- Experience in using relational databases and understanding of database concepts
- Computer programming experience
- Experience in database server management, operating system management, or network administration

#### Organization

This manual has been organized as follows:

-   Chapter 1: Introduction 
    This chapter introduces the concepts, features, and architecture of the Altibase server.
    
-   Chapter 2: Altibase Components 
    This chapter describes the components of the executable binaries and programming libraries that make up Altibase.
    
-   Chapter 3: Creating a Database
    This chapter describes the types of tablespaces and logging system that are representative components of a database, and how to create a database.
    
-   Chapter 4: Altibase Startup and Shutdown
    This chapter describes how to startup and shutdown Altibase, and explains what to do internally during Altibase multi-state startup.
    
-   Chapter 5: Database Objects and Privileges 
    This chapter describes Altibase objects and privileges such as constraints, indexes, sequences, replication, tables, and users. This chapter also describes the privileges of the system and schema object levels.
    
-   Chapter 6: Managing Tablespaces 
    This chapter describes how to manage the database's logical structure in small units and manage the physical data space more efficiently. 
    
-   Chapter 7: Partitioned Objects 
    This chapter describes partitioned tables. Partitioned tables are managed by breaking a large database table into smaller tables.
    
-   Chapter 8: Managing Transactions
  
    This chapter describes the concepts behind transactions and locking, and explains how to manage transactions in the Altibase server.

-   Chapter 9: Database Buffer Manager
  
    This chapter describes the structure and functions of the buffer manager.
    
-   Chapter 10: Backup and Recovery
  
    This chapter describes the Altibase backup and recovery features and explains how to manage your database backup and recovery tasks.
    
-   Chapter 11: Incremental Backup and Recovery
  
    This chapter explains incremental backup and recovery provided by Altibase.

-   Chapter 12: Server/Client Communication
  
    This chapter describes the connection methods and protocols between the Altibase server and client application.

-   Chapter 13: Altibase Security
  
    This chapter describes Altibase's security features for protecting database information.

-   Chapter 14: Auditing Altibase
  
    This chapter describes the auditing feature which tracks and writes logs in real time of statements running on the Altibase server.

-   Chapter 15: Tuning Altibase
  
    This chapter describes log file groups and group commits to improve the performance of Altibase.

-   Chapter 16: Monitoring Altibase and PBT
  
    This chapter explains how to monitor and troubleshoot database servers. In addition, it describes the checklist and analysis method of various problems that may occur when Altibase is running. 
    
-   Appendix A: Trace Logs
  
    This appendix describes application trace logs and explains how to create and access them.
    
-   Appendix B: Altibase Limitations
  
    This appendix describes the maximum values of Altibase objects.

#### Documentation Conventions

This section describes the conventions used in this manual. Understanding these conventions will make it easier to find information in this manual and other manuals in the series.

There are two sets of conventions:

- Syntax diagrams
- Sample code conventions

##### Syntax diagrams

This manual describes command syntax using diagrams composed of the following elements:

| Elements                                   | Meaning                                                      |
| ------------------------------------------ | ------------------------------------------------------------ |
| ![image1](../media/GettingStarted/image1.gif) | Indicates the start of a command. If a syntactic element starts with an arrow, it is not a complete command. |
| ![image2](../media/GettingStarted/image2.gif) | Indicates that the command continues to the next line. if a syntactic element ends with this symbol, it is not a complete command. |
| ![image3](../media/GettingStarted/image3.gif) | Indicates that the command continues from the previous line. If a syntactic element starts with this symbol, it is not a complete command. |
| ![image4](../media/GettingStarted/image4.gif) | Indicates the end of a statement.                            |
| ![](../media/Admin/image012.gif)              | Indicates a mandatory element.                                                    |
| ![image6](../media/GettingStarted/image6.gif) | Indicates an optional element.                               |
| ![image7](../media/GettingStarted/image7.gif) | Indicates a mandatory element comprised of options. One, and only one, option must be specified. |
| ![image8](../media/GettingStarted/image8.gif) | Indicates an optional element comprised of options           |
| ![image9](../media/GettingStarted/image9.gif) | Indicates an optional element in which multiple elements may be specified. A comma must precede all but the first element. |

##### Sample Code Conventions

The code examples explain SQL, stored procedures, iSQL, and other command line syntax.

The following describes the conventions used in the cod examples:

| Rules            | Meaning                                                      | Example                                                      |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [ ]              | Indicates an optional item                                   | VARCHAR [(*size*)] [[FIXED \|] VARIABLE]                     |
| { }              | Indicates a mandatory field for which one or more items must be selected. | { ENABLE \| DISABLE \| COMPILE }                             |
| \|               | A delimiter between optional or mandatory arguments.         | { ENABLE \| DISABLE \| COMPILE } [ ENABLE \| DISABLE \| COMPILE ] |
| . . .            | Indicates that the previous argument is repeated, or that sample code has been omitted. | SQL\> SELECT ename FROM employee;<br/> ENAME<br/>  -----------------------<br/> SWNO<br/>  HJNO<br/>  HSCHOI<br/>  .<br/> .<br/> .<br/> 20 rows selected. |
| Other Symbols    | Symbols other than those shown above are part of the actual code. | EXEC :p1 := 1; acc NUMBER(11,2)                              |
| Italics          | Statement elements in italics indicate variables and special values specified by the user. | SELECT \* FROM *table_name*; <br/>CONNECT *userID*/*password*; |
| Lower case words | Indicate program elements set by the user, such as table names, column names, file names, etc. | SELECT ename FROM employee;                                  |
| Upper case words | Keywords and all elements provided by the system appear in upper case. | DESC SYSTEM_.SYS_INDICES_;                                   |

#### 

#### Related Documents

Please refer to the following documents for more detailed information:

-   Installation Guide

-   Getting Started Guide

-   SQL Reference

-   Stored Procedures Manual

-   iSQL User’s Manual

-   Utilities Manual

-   Error Message Reference

#### Altibase Welcomes Your Comments and Feedback

Please let us know what you like or dislike about our manuals. To help us with better future versions of our manuals, please tell us if there are any corrections or classifications that you would find useful.

Include the following information:

- The name and version of the manual that you are using
- Any comments about the manual
- Your name, address, and phone number

If you need immediate assistance regarding any errors, omissions, and other technical issues, please contact [Altibase's Support Portal](http://support.altibase.com/en/).

Thank you. We always welcome your feedback and suggestions.

